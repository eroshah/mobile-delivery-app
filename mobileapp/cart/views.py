from django.shortcuts import render

from . import models
from . import serializers
from stores.models import Item

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from decimal import Decimal


# Create your views here.

class CartView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        if request.user.is_anonymous:
            return Response({'detail':'Login to add item to your cart.'},status=status.HTTP_401_UNAUTHORIZED)
        objects = models.Cart.objects.get(user=request.user)
        serializer = serializers.GetCartSerializer(objects)
        return Response(serializer.data,status=status.HTTP_200_OK)



class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request,pk):
        serializer = serializers.GetCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            item = Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Response({'detail': f'Product with id={item.id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        quantity = request.data['quantity']
        subtotal = int(item.price) * int(quantity)
        cart = models.Cart.objects.get(user=request.user)


        cartitem = models.CartItem.objects.create(
                item=item,
                quantity=quantity,
                subtotal=subtotal,
                cart=cart)
        cartitem.save()

        all = models.CartItem.objects.filter(cart=cart)
        total_price = sum([int(i.subtotal) for i in all])
        cart_quantity = sum([j.quantity for j in all])

        cart = models.Cart.objects.filter(user=request.user).update(total_price=total_price,cart_quantity=cart_quantity)

        return Response({'detail': 'Product added to cart.'}, status=status.HTTP_201_CREATED)

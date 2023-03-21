from django.shortcuts import render

from . import serializers
from . import models

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class StoreView(APIView):

    def get(self,request):
        objects = models.Store.objects.all()
        serializer = serializers.GetStoreSerializer(objects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = serializers.GetStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ItemView(APIView):

    def get(self,request):
        objects = models.Item.objects.all()
        serializer = serializers.GetItemSerializer(objects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = serializers.GetItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StoreItemView(APIView):

    def get(self,request,pk):
        objects = models.Store.objects.get(id=pk)
        serializer = serializers.GetStoreItemSerializer(objects)
        return Response(serializer.data,status=status.HTTP_200_OK)

class StoreInfoView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,pk):
        objects = models.Store.objects.get(id=pk)
        serializer  = serializers.GetStoreInfoSerializer(objects)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,pk):
        request.data._mutable = True
        request.data.update({"store":f"{pk}" , "User": f"{request.user.id}"})
        serializer = serializers.GetRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

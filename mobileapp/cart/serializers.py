from rest_framework import serializers

from stores.serializers import GetItemSerializer
from stores.models import Item
from . import models

class GetCartSerializer(serializers.ModelSerializer):
    cart_item = serializers.SerializerMethodField()

    class Meta:
        model = models.Cart
        fields = ['id','user_id','total_price','cart_quantity','cart_item']

    def get_cart_item(self,obj):
        cart_item = models.CartItem.objects.filter(cart=obj)
        return GetCartItemSerializer(cart_item,many=True).data



class GetCartItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = models.CartItem
        fields = ['id','quantity','subtotal','item']

    def get_item(self,obj):
        item = Item.objects.filter(cartitem=obj)
        return GetItemSerializer(item,many=True).data

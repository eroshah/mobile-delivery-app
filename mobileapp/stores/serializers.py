from rest_framework import serializers
from . import models

class GetStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = '__all__'

class GetStoreItemSerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField()

    class Meta:
        model = models.Store
        fields=['id','name','adress','phone_number','orders','payment_method','cuisine','fast_delivery','description','image','foods']

    def get_foods(self,obj):
        foods = models.Item.objects.filter(store=obj)
        return GetItemSerializer(foods,many=True).data


class GetStoreInfoSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = models.Store
        fields = ['id','name','adress','phone_number','orders','payment_method','cuisine','fast_delivery','description','image','ratings']

    def get_ratings(self,obj):
        ratings = models.Rating.objects.filter(store=obj)
        return GetRatingSerializer(ratings,many=True).data

class GetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'


class GetRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = ['rate','comment','published_date','store','User']

from django.db import models
from django.db.models import JSONField
from django.utils import timezone
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User

# Create your models here.
class Store(models.Model):

    name = models.CharField(max_length=36)
    adress = models.CharField(max_length=36)
    phone_number = models.IntegerField()
    orders = models.IntegerField()
    payment_method = models.CharField(max_length=10)
    cuisine = models.CharField(max_length=36,null=True,blank=True)
    fast_delivery = models.BooleanField()
    description = models.TextField()
    image = models.ImageField()


    def __str__(self):
        return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self):
        return self.name

class Item(models.Model):

    category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=36)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    portion = models.CharField(max_length=36,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    cuisine = models.CharField(max_length=36,null=True,blank=True)
    is_available = models.BooleanField()
    vegan = models.BooleanField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

rates = (
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),)

class Rating(models.Model):

    rate = models.IntegerField(choices=rates)
    comment = models.TextField(max_length=120,null=True,blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    User = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.store.name+" " + str(self.rate)

from django.db import models
from django.contrib.auth import get_user_model
from stores.models import Item
from decimal import Decimal

# Create your models here.

User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='cart')
    total_price = models.DecimalField(max_digits=9,decimal_places=2,default=0.00)
    cart_quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.user}\'s Cart {self.id}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.item} - {self.quantity}'

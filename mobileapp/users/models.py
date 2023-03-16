from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import MyAccountManager

from location_field.models.plain import PlainLocationField


# Create your models here.
class User(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", max_length=68, unique=True)
    username = models.CharField(max_length=36, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name= 'last login', auto_now=True)
    is_admin = models. BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='image',blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', "first_name", "last_name"]

    objects = MyAccountManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Adress(models.Model):
    name = models.CharField(max_length=36)
    country = models.CharField(max_length=36)
    city = models.CharField(max_length=36)
    street = models.CharField(max_length=36)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

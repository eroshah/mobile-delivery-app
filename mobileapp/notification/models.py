from django.db import models
from users.models import User

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.title

class SendedNotification(models.Model):
    type = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250,null=True,blank=True)
    image = models.ImageField(upload_to=None,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notif_receiver')
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(to='stores.Item',on_delete=models.CASCADE,null=True,blank=True)
    related_user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='notif_sender',null=True,blank=True)

    def __str__(self):
        return self.content

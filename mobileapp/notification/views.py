from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from . import models,serializers

import _thread as thread

# Create your views here.
def send_notification(msg,users,type,obj,img=None,title=None):
    try:
        thread.start_new_thread(log_notifications,(users,msg,type,obj,img,title))
        devices = FCMDevice.objects.filter(user__pk__in=users)
        devices.send_message(title='Title',body=msg)
    except:
        pass

def log_notifications(users,msg,type,obj,img,title):
    for user in users:
        try:
            user = User.objects.get(pk=user['user'])
        except:
            pass
        if type == 'item' or type == 'live' or type == 'message':
            models.SendedNotification.objects.create(type=type,user=user,content=msg,item=obj,image=img,subtitle=title)

class SendedNotificationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        notifications= models.SendedNotification.objects.filter(user=request.user),order_by('-pk')
        serializer = serializers.SendedNotificationSerializer(notifications,many=True)
        return Response(serializer.data)

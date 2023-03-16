from rest_framework import serializers
from . import models


class SendedNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SendedNotification
        fields = '__all__'

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken,TokenError
from rest_framework_simplejwt.exceptions import InvalidToken

from django.contrib.auth.password_validation import validate_password

from . import models


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=models.User.objects.all())]
            )

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = ('password1', 'password2', 'email','username', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = models.User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )


        user.set_password(validated_data['password1'])
        user.save()

        return user

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError('User with this email does not exist')
        else:
            raise serializers.ValidationError('Email is required')

        return attrs

User = get_user_model()

class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128,validators=[validate_password])
    confirm_password = serializers.CharField(max_length=128)
    token = serializers.CharField(max_length=255)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        token = attrs.get('token')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')

        try:
            token = UntypedToken(token)
            token.verify()
        except (TokenError, InvalidToken):
            raise serializers.ValidationError('Invalid token')

        user_id = token['user_id']
        user = User.objects.filter(id=user_id, is_active=True).first()

        if user is None:
            raise serializers.ValidationError('Invalid token')

        attrs['user'] = user
        return attrs

    def save(self):
        user = self.validated_data.get('user')
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()

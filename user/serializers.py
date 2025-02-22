from .models import SMSCode
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)

def validate(self, data):
    if data['password'] != data['confirm_password']:
        raise serializers.ValidationError('passwords do not match')
    return data

def validate_username(self, username):
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
         return username
    raise serializers.ValidationError('Username already taken')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class SMSCodeSerializer(serializers.Serializer):
    sms_code = serializers.CharField(max_length=100)
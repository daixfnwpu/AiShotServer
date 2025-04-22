from django.contrib.auth.models import AbstractUser, AbstractUser, Group, Permission
from django.db import models
from rest_framework import serializers

from AiShotServer.models import CustomUser

class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['avatar']



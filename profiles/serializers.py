from rest_framework import serializers
from .models import *


class UserNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNet
        exclude = ('is_active', 'is_staff', 'is_superuser', 'last_login', 'password',
                   'user_permissions', 'groups', )


class FollowerProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('username', 'avatar', 'first_name', 'last_name', )

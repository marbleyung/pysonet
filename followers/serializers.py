from rest_framework import serializers
from .models import Follower
from profiles.serializers import FollowerProfileSerializer


class FollowerSerializer(serializers.ModelSerializer):
    subscriber = FollowerProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber', )



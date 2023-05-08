import profiles.models
from .serializers import *
from rest_framework import generics, response
from rest_framework import permissions
from .models import Follower


class FollowerView(generics.ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(generics.CreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = profiles.models.UserNet.objects.filter(id=pk)
        if user:
            Follower.objects.create(user=user[0], follower=self.request.user)
            return response.Response(status=201)
        return response.Response(status=404)

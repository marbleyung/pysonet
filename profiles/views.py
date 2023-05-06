from .serializers import *
from rest_framework import permissions
from rest_framework import viewsets


class UserNetViewset(viewsets.ModelViewSet):
    queryset = UserNet.objects.all()
    serializer_class = UserNetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes_by_action = {'get': [permissions.AllowAny],
    #                                 'put': [permissions.IsAuthenticated]}
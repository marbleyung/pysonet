from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import RetrieveAPIView


class GetUserNetView(RetrieveAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserNetSerializer
from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('user/<int:pk>/', UserNetViewset.as_view({'get': 'retrieve', 'put': 'update'})),
    path('users/', UserNetViewset.as_view({'get': 'list'}))
]

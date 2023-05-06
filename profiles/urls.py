from .views import *
from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('user/<int:pk>/', GetUserNetView.as_view())
]

from django.urls import path
from .views import *


urlpatterns = [
    path('', FollowerView.as_view()),
    path('follow/<int:pk>/', AddFollowerView.as_view()),
]

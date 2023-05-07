from django.urls import path, include


urlpatterns = [
    path('', include('profiles.urls')),
    path('wall/', include('wall.urls')),
]

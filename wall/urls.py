from django.urls import path, include
from . import views


urlpatterns = [
    path('post-list/<int:pk>/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostView.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'delete': 'destroy',
                                                   'post': 'create'})),
    path('comment/<int:pk>/', views.CommentView.as_view({'get': 'retrieve',
                                                         'put': 'update',
                                                         'delete': 'destroy',
                                                         'post': 'create'})),
    path('comment-list/<int:pk>/', views.CommentListView.as_view())
]

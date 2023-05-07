import rest_framework.generics
from rest_framework import permissions

from base.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from base.permissions import IsAuthor
from .serializers import *


class PostListView(rest_framework.generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(author_id=self.kwargs.get('pk'))


class CommentListView(rest_framework.generics.ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.filter(author_id=self.kwargs.get('pk'))


class PostView(CreateRetrieveUpdateDestroy):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(CreateRetrieveUpdateDestroy):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



from rest_framework import serializers

from base.serializers import RecursiveSerializer, FilterCommentListSerializer
from .models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', "text", 'parent',)


class CommentListSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "text", "created_at", "edited_at", "children")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "created_at", "author", "text", "comments", 'times_viewed')


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ("id", "created_at", "author", "text", 'times_viewed', 'comments_count')

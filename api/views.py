from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    lookup_fields = ('post', 'id')

    def get_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id']).comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(
            author=self.request.user, 
            post_id=post.id
            )

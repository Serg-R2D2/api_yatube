from rest_framework import serializers
from posts.models import Post, Comment



class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment

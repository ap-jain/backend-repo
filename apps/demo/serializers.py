from rest_framework import serializers
from .models import Post, Comment

# Serializer for the Comment model
class CommentSerializer(serializers.ModelSerializer):
    # Serializing the author's username (related field from the User model)
    author_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'author_username']

# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    # Adding the count of comments related to this post
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    # Serializing the author's username (related field from the User model)
    author_username = serializers.CharField(source='user.username', read_only=True)
    
    # This field will be a nested list of serialized comments (up to 3 latest comments)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'comment_count', 'author_username', 'comments']

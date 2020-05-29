""""Serializers for Categories"""

from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Set the fields to be use in the view file"""
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user_id', 'news_id', 'deleted')
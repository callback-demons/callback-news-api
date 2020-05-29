""""Serializers for News"""

from rest_framework import serializers

from .models import News
#from comments.models import Comment
'''
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'user')
'''
class NewsSerializer(serializers.ModelSerializer):
    """Set the fields to be use in the view file"""
    class Meta:
        model = News
        fields = (
            'id',
            'slug',
            'title',
            'author',
            'description',
            'created',
            'date_posted',
            'likes',
            'media',
            'source',
            'category'
        )
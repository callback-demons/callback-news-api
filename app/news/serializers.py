""""Serializers for News"""

from rest_framework import serializers

from .models import News
from categories.models import Category
from sources.models import Source
from media.models import Media

'''
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'user')
'''

class MediaSerializer(serializers.ModelSerializer):
    """Set the fields to be use in the view"""

    class Meta:
        model = Media
        fields = ('id',
                  'title',
                  'type',
                  'url')

class CategorySerializer(serializers.ModelSerializer):
    """Set the fields to be use in the view"""

    class Meta:
        model = Category
        fields = ('id',
                  'name')

class SourceSerializer(serializers.ModelSerializer):
    """Set the fields to be use in the view"""

    class Meta:
        model = Source
        fields = ('name',
                  'url',
                  'disclaimer',
                  'logo')

class NewsSerializer(serializers.ModelSerializer):
    """Set the fields to be use in the view file"""
    category = CategorySerializer(read_only=True)
    source = SourceSerializer(read_only=True)
    media = MediaSerializer(many=True)

    class Meta:
        model = News
        fields = ('id',
                  'slug',
                  'title',
                  'author',
                  'description',
                  'created',
                  'date_posted',
                  'likes',
                  'content',
                  'media',
                  'source',
                  'category')


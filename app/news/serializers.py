""""Serializers for News"""

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import News, Likes
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
    likes = serializers.SerializerMethodField()

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

    def get_likes(self, instance):
        request_object = self.context['request']
        count = Likes.objects.filter(news=instance).count()

        if request_object.user.is_anonymous:
            liked = False
        else:
            liked = Likes.objects.filter(news=instance, user=request_object.user).count() > 0

        return {
            'count': count,
            'liked': liked
        }


class NewsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5
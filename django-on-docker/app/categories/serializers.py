""""Serializers for Categories"""

from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """Set the fields to be use in the view file"""
    class Meta:
        model = Category
        fields = ('name', 'color', 'image', 'deleted')
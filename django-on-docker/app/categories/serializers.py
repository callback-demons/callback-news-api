""""Serializers for Categories"""

from rest_framework import serializers

from api.categories.models import Category

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('name', 'color', 'image', 'deleted')
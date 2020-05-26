"""Categories views."""

from django.shortcuts import render

#Models
from api.categories.models import Category

#Serializers
from api.categories.serializers import CategorySerializer

@api_views(['GET'])
def list_categories(request):
    """Return a list of all the categories."""
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(delete__isnull=False)
    




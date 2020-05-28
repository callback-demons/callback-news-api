"""Categories views."""
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from news.models import News
from news.serializers import NewsSerializer
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Categories Model.
    """
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_news(request, id):
    """
    A function that gets news from a category id
    """
    get_object_or_404(Category, id=id)
    queryset = News.objects.filter(category=id, deleted__isnull=True)
    serializer = NewsSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

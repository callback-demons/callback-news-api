"""News views."""
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import NewsSerializer, NewsPagination
from .models import News, LikeUsers


class NewsViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for News Model.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, news_id):
    """
    Set or unset like from news
    """
    news = get_object_or_404(News, id=news_id)
    try:
        like_user = LikeUsers.objects.get(user_id=request.user, news_id=news)
        like_user.delete()
        return JsonResponse({"message": "removed like to news"})
    except LikeUsers.DoesNotExist:
        like_user = LikeUsers(user_id=request.user, news_id=news)
        like_user.save()
        return JsonResponse({"message": "added like to news"})

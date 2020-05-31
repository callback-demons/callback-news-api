"""News views."""
from django.db.models import Count
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import NewsSerializer, NewsPagination
from .models import News, Likes


class NewsViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for News Model.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        queryset = News.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__contains=title)
        return queryset


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, news_id):
    """
    Set or unset like from news
    """
    news = get_object_or_404(News, id=news_id)
    try:
        likes = Likes.objects.get(user=request.user, news=news)
        likes.delete()
        return JsonResponse({"message": "removed like to news"})
    except Likes.DoesNotExist:
        likes = Likes(user=request.user, news=news)
        likes.save()
        return JsonResponse({"message": "added like to news"})


class NewsPopularViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for News Model.
    """
    top_popular = query = Likes.objects.values('news_id').annotate(likes=Count('news_id')).order_by('-likes')[:10]
    queryset = News.objects.filter(id__in=top_popular.values_list('news_id'))
    serializer_class = NewsSerializer


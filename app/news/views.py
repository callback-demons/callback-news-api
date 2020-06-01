"""News views."""
from datetime import datetime

from django.db.models import Count
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from media.models import Media
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
            queryset = queryset.filter(title__icontains=title)
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

class NewsbyDateViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides news sorted by published date.
    """
    queryset = News.objects.order_by('published')[:10]
    serializer_class = NewsSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def publish(request):
    """
    publish a news
    """
    media = Media(url=request.data['media'], title=request.data['title'])
    media.save()
    news = News(user=request.user, title=request.data['title'])
    news.date_posted = request.data['date_posted']
    news.category_id = request.data['category_id']
    news.source_id = request.data['source_id']
    news.author = request.data['author']
    news.description = request.data['description']
    news.content = request.data['content']
    if 'published' in request.data:
        news.published = datetime.now()
    news.save()
    news.media.set([media.id])
    serializer = NewsSerializer(news, many=False, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

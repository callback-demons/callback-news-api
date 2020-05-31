"""Categories views."""
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from news.models import News
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Comment Model.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comments(request, news_id):
    """
    A function that get or post a comments in news
    """
    get_object_or_404(News, id=news_id)
    if request.method == 'GET':
        return get_comments(request, news_id)
    if request.method == 'POST':
        return post_comment(request, news_id)


def get_comments(request, news_id):
    """
    A function that get comments from news
    """
    comment = Comment.objects.filter(news_id=news_id, deleted__isnull=True)
    serializer = CommentSerializer(comment, many=True)
    return JsonResponse(serializer.data, safe=False)


def post_comment(request, news_id):
    """
    A function that post a comment in news
    """
    if 'content' not in request.data:
        raise ValidationError('field content is required')
    if request.data['content'] == '':
        raise ValidationError('content field should be not empty')
    comment = Comment(content=request.data['content'],
                      user_id=request.user.id,
                      news_id=news_id)
    comment.save()
    serializer = CommentSerializer(comment, many=False)
    return JsonResponse(serializer.data, safe=False)

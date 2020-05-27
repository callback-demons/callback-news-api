"""Categories views."""

from django.shortcuts import render
from rest_framework import viewsets  
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Comment Model.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    




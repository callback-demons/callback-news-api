"""News views."""

from django.shortcuts import render
from rest_framework import viewsets  
from .serializers import NewsSerializer
from .models import News


class NewsViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for News Model.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer

    
    




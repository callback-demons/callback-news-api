"""Categories views."""

from django.shortcuts import render
from rest_framework import viewsets  
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Categories Model.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    




from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Source
from .serializers import SourceSerializer


class SourcesViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Source Model.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

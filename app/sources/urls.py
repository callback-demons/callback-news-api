"""Urls routes for News"""

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sources', views.SourcesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

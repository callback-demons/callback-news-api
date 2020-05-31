"""Urls routes for News"""

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'news-popular', views.NewsPopularViewSet)
router.register(r'news-date', views.NewsbyDateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('news/<int:news_id>/like', views.like, name="like"),
    path('news-publish', views.publish, name="publish")
]
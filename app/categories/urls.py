""""Urls routes for Categories"""

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path("categories/<int:id>/news/", views.get_news, name="get_news"),
]
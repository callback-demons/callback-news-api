""""Urls routes for Categories"""

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("news/<int:id>/comments/", views.comments, name="comments"),

]

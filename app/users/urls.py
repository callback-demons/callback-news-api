""""Urls routes for Categories"""

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('account/register', views.CreateUserView.as_view()),
    path('account/update', views.UpdateUserView.as_view()),
]

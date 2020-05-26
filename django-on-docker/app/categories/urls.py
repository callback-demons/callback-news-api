from django.urls import include, path
from rest_framework import routers
from categories import views

router = routers.DefaultRouter()
router.register(r'categories', views.list_categories)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.urls import path

from .views import list_categories

urlpatterns = [
    path('caegory/', api.categories.list_category.as_view(), name='api-post-details'),
]
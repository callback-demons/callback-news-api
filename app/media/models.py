"""Media model"""

#Django
from django.db import models

#Utilities
from api.utils.models import APImodels

class Media(APImodels):
    """Media Model.
    
    Media associated to the content of a single article.
    """

    title = models.TextField()
    type = models.CharField(max_length=50)
    url = models.TextField(null=True)

    class Meta(object):
        verbose_name_plural = 'Media'
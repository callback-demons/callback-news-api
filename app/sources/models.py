"""Sources model"""

#Django
from django.db import models

#Utilities
from api.utils.models import APImodels

class Source(APImodels):
    """Sources Model.
    
    Provides the information of the sites that are used to scrapping.
    """

    name = models.CharField('source name', max_length=200)
    url = models.CharField('source url', max_length=2048)
    logo = models.ImageField(
        'media logo',
        upload_to='users/pictures/',
        blank=True,
    )
    disclaimer = models.TextField(blank=True)  

    def __str__(self):
        return self.name  

    class Meta(object):
        verbose_name_plural = 'Sources'


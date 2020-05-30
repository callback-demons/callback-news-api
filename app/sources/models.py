"""Sources model"""

# Django
from django.db import models

# Utilities
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

    FEED_TYPES = [
        ('rss1', 'RSS1'),
        ('rss2', 'RSS2'),
        ('atom', 'ATOM'),
        ('html', 'HTML'),
        ('json', 'JSON'),
    ]

    feed_url = models.CharField('feed url', max_length=2048, default='')

    feed_type = models.CharField('feed type',
                                 max_length=4,
                                 choices=FEED_TYPES,
                                 default='rss2',
                                 )

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name_plural = 'Sources'

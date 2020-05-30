"""Media model"""

# Django
from django.db import models

# Utilities
from api.utils.models import APImodels


class Media(APImodels):
    """Media Model.
    
    Media associated to the content of a single article.
    """

    image = 'image'
    video = 'video'
    audio = 'audio'
    slides = 'slides'
    other = 'other'

    TYPE_OF_CONTENT = [
        (image, 'image'),
        (video, 'video'),
        (audio, 'audio'),
        (slides, 'slides'),
        (other, 'other'),
    ]

    title = models.CharField(max_length=500)

    type = models.CharField(max_length=50,
                            choices=TYPE_OF_CONTENT,
                            default=image,
                            )

    url = models.CharField(null=True, max_length=2048)

    news_related = models.ForeignKey('news.News',
                                     related_name='media_news',
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE,
                                     )

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name_plural = 'Media'

"""News model"""

#Django
from django.db import models

#Utilities
from api.utils.models import APImodels

class News(APImodels):
    """News Model.
    
    Define the structure for the news that are feeded by the scrapper.
    """

    title = models.TextField()
    author = models.TextField()
    description = models.TextField(null=True)
    slug = models.TextField(null=True)
    content = models.TextField()
    date_posted = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(null=True, auto_now_add=True,)
    published = models.DateTimeField(null=True,)


    #Foreing keys
    user =  models.ForeignKey('users.User',
            null=True,
            on_delete=models.CASCADE,
            )

    media = models.ManyToManyField('media.Media',
            null=True,
            related_name='news_media'
            )

    category =  models.ForeignKey('categories.Category',
                null=True,
                on_delete=models.CASCADE,
                )

    source =    models.ForeignKey('sources.Source', 
                null=True,
                on_delete=models.CASCADE)
    
    class Meta(object):
        verbose_name_plural = 'News'
"""News model"""

#Django
from django.db import models

#Utilities
from api.utils.models import APImodels

class News(APImodels):
    """News Model.
    
    Define the structure for the news that are feeded by the scrapper.
    """

    title = models.CharField('news title', max_length=500)
    author = models.CharField('author name(s)', max_length=500)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(null=True, max_length=500)
    content = models.TextField()
    date_posted = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(null=True, auto_now_add=True,)
    published = models.DateTimeField(null=True, blank=True,)

    #Foreing keys
    user =  models.ForeignKey('users.User',
            null=True,
            on_delete=models.CASCADE,   
            )

    media = models.ManyToManyField('media.Media',
            null=True,
            blank=True,
            related_name='news_media',
            )

    category =  models.ForeignKey('categories.Category',
                null=True,
                on_delete=models.CASCADE,
                )

    source =    models.ForeignKey('sources.Source', 
                null=True,
                on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name_plural = 'News'
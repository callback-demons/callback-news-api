"""Comments model"""

#Django
from django.db import models

#Utilities
from api.utils.models import APImodels

class Comment(APImodels):
    """Comments Model.
    
    Refers to the comments that an user make in an article.
    """

    content = models.TextField()

    #Foreing Keys
    user = models.ForeignKey('users.User', 
            on_delete=models.CASCADE)
        
    news =  models.ForeignKey('news.News', 
            on_delete=models.CASCADE, 
            null=True,
            blank=True
            )

    def __str__(self):
        return self.content

    class Meta(object):
        verbose_name_plural = 'Comments'    

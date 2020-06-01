"""Categories model"""

#Django
from django.db import models

#Utilities
from api.utils.models import APImodels

class Category(APImodels):
        """Category Model.

        Stores the categories to classify the news
        """
        name =  models.CharField('category name', 
                max_length=150)

        color = models.CharField('color assigned', 
                max_length=7, 
                null=True)

        picture = models.ImageField('category image', 
                upload_to='users/pictures/',
                null=True
                )

        def __str__(self):
                return self.name


        class Meta(object):
                verbose_name_plural = 'categories'
"""News model"""

# Django
from django.db import models
from django.template.defaultfilters import slugify

# Utilities
from api.utils.models import APImodels


class LikeUsers(models.Model):
    """
    Structure for like logic model
    """
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    news_id = models.ForeignKey('news.News', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class News(APImodels):
    """News Model.

    Define the structure for the news that are feeded by the scrapper.
    """

    title = models.CharField('news title', max_length=500)
    author = models.CharField('author name(s)', max_length=500)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(null=True, auto_now_add=True, )
    published = models.DateTimeField(null=True, blank=True, )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


    # Foreing keys
    user = models.ForeignKey('users.User',
                             null=True,
                             on_delete=models.CASCADE,
                             )

    media = models.ManyToManyField('media.Media',
                                   blank=True,
                                   related_name='news_media',
                                   )

    category = models.ForeignKey('categories.Category',
                                 null=True,
                                 on_delete=models.CASCADE,
                                 )

    source = models.ForeignKey('sources.Source',
                               null=True,
                               on_delete=models.CASCADE)

    likes_users = models.ManyToManyField('users.User', related_name='likes', through=LikeUsers)

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name_plural = 'News'
"""Django models utilities."""

from django.db import models

class APImodels(models.Model):
    """
        APImodels is an abstract base class that inheritothers model of the project.
        This class provide table with the following attribute:
            - created(DateTime): store datetime when an object was created. 
            - modified(DateTime): store las datetime when an object was modified. 
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time when object was created'
    )

    deleted = models.DateTimeField(
        'deleted at',
        null=True,
        blank=True,
        help_text='Date time when object was deleted'
    )

    class Meta:
        """Meta option"""

        abstract = True 
        get_latest_by='created'
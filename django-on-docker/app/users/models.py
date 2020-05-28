"""User model"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from api.utils.models import APImodels

class User(APImodels, AbstractUser):
    """User Model.
    
    Extend from Django's Abatract user and add fields required for the model
    """

    email_validator = RegexValidator(
        regex=r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
        message="Make sure your mail looks something like this: user@domain.com."
    )

    email = models.EmailField(
        'email address',
        unique = True,
        validators=[email_validator],
        error_messages={
            'unique': 'Ops!, This email already exist.'
        }
    )

    birth_date = models.DateField()
    country = models.TextField()
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'birth_date', 'country']

    is_reader = models.BooleanField(
        'reader',
        default=True,
        help_text=(
            'Help easily distinguish readers and perform queries. '
            'Readers are the main type of user.'
        )
    )

    is_moderator = models.BooleanField(
        'reader',
        default=False,
        help_text=(
            'Help easily distinguish moderators and perform queries. '
            'Moderators are a type of user to manage CMS.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )
    
    
    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username





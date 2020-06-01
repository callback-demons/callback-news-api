"""Test for users app"""
from django.test import TestCase
from .models import User

class UserModelTest(TestCase):

    def test_user_fields(self):
        """
        inserts fields in the model.
        """
        username= User(username="Gerardo-marquez")
        self.assertEqual(str(username), username.username)
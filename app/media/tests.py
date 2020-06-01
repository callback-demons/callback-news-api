"""Test for categories  app"""
from django.test import TestCase
from .models import Media

class MediaModelTest(TestCase):

    def test_media_fields(self):
        """
        inserts fields in the model.
        """
        title= Media(title="Quatum computer of IBM")
        self.assertEqual(str(title), title.title)
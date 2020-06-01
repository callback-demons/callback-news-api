"""Test for news  app"""
from django.test import TestCase
from .models import News

class NewsModelTest(TestCase):

    def test_news_field(self):
        """
        inserts fields in the model.
        """
        title= News(title="Google launch recent cloud services")
        self.assertEqual(str(title), title.title)
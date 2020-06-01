"""Test for sources  app"""
from django.test import TestCase
from .models import Source

class SourcesModelTest(TestCase):

    def test_sources_fields(self):
        """
        inserts fields in the model.
        :return:
        """
        name= Source(name="El Espectador")
        self.assertEqual(str(name), name.name)

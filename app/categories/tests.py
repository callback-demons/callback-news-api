"""Test for categories  app"""
from django.test import TestCase
from .models import Category

class CategoriesModelTest(TestCase):

    def test_string_representation(self):
        """
        inserts fields in the model.
        :return:
        """
        name= Category(name="5g")
        self.assertEqual(str(name), name.name)

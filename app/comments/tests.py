"""Test for comments app"""
from django.test import TestCase
from .models import Comment

class CategoriesModelTest(TestCase):

    def test_string_representation(self):
        name= Comment(name="5g")
        color = Category(color="#029645")
        self.assertEqual(str(name), name.name)
        self.assertEqual(str(color), color.color)
from datetime import datetime
import unittest
from category.domain.entities import Category


class TestCategory(unittest.TestCase):

    def test_constructor(self):
        Category = Category('Movie', 'some description', True, datetime.now())
        self.assertEqual(Category.name, 'Movie')
        self.assertEqual(Category.description, 'some description')
        self.assertEqual(Category.enabled, True)
        self.assertEqual(Category.created_at, datetime.now())
        
import unittest
from category.domain.entities import Category


class TestCategory(unittest.TestCase):

    def test_constructor(self):
        Category(Category('Movie', 'some description', True, datetime.now()))
        
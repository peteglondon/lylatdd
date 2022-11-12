import unittest
from app.cat import Cat

class TestAnimals(unittest.TestCase):

    def test_cat_says_meow_with_name(self):
        cat = Cat("Floofy")
        self.assertEqual("Meow I'm Floofy", cat.introduce_yourself())

    def test_cat_says_meow(self):
        cat = Cat("Floofy")
        self.assertEqual("Meow", cat.speak())

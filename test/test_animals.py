import unittest
from app.cat import Cat
from app.dog import Dog

class TestAnimals(unittest.TestCase):

    def test_cat_says_meow_with_name(self):
        cat = Cat("Floofy")
        self.assertEqual("Meow I'm Floofy", cat.introduce_yourself())

    def test_cat_says_meow(self):
        cat = Cat("Floofy")
        self.assertEqual("Meow", cat.speak())

    def test_dog_says_woof(self):
        dog = Dog("Bob")
        self.assertEqual("Woof", dog.speak())

    def test_dog_says_woof_with_name(self):
        dog = Dog("Bob")
        self.assertEqual("Woof I'm Bob", dog.introduce_yourself())

import os
from .banana_recipes_test import TestBananaRecipes

class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        self.assertEqual("The recipe for a classic banana pudding is ready.", "Bakery in the City")

if __name__ == '__main__':
    unittest.main()

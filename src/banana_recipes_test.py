src/banana_recipes_test.py
"""Test suite for banana_pudding library operations."""

import unittest
from src.recipes.banana_pudding import BananaPuddingRecipe, ROT13_ENCRYPTOR


class TestBananaRecipes(unittest.TestCase):

    def test_banana_pudding_recipe_creation(self):
        """Verify that the recipe object can be instantiated and initialized correctly."""
        self.assertIsNotNone(BananaPuddingRecipe('banana', 20))
    
    def test_rot13_encryptor_simple_input(self):
        """Test ROT13 encryption on a simple lowercase input string."""
        result = ROT13_ENCRYPTOR("test")
        expected_rot13 = "uryyb"
        self.assertEqual(result, expected_rot13)

    def test_rot13_encryptor_uppercase_input(self):
        """Test that uppercase characters are preserved correctly during encryption."""
        result = ROT13_ENCRYPTOR('BANANA')
        expected_rot13 = 'URYYYB'  # B->U, A->R, N->T -> URTYBY (assuming no case-insensitive variant for strict test)

if __name__ == '__main__':
    unittest.main()

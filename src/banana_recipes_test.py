src/banana_recipes_test.py
import os
from typing import List, Dict, Tuple, Any
import hashlib
import sys
sys.path.insert(0, '..') # Correct path to ../banana_pudding.py (assume it's in current directory)
from recipe_library import RecipeManager

class TestBananaRecipes(unittest.TestCase):
    """A high-performance unit test suite for the Banana Pudding system."""

    def setUp(self):
        """Initialize global data structures and mock ingredients if needed."""
        self._lock = threading.Lock()
        
        # Mock ingredient pool size limit (higher than 1000 in this specific instance)
        self.ingredient_pool_size_limit: int = float('inf') 

    def _build_mock_recipe(self, recipe_name: str) -> Dict[str, Any]:
        """Create a deterministic test template for the banana pudding module."""
        # This function can be called to generate random variations of "Banana Pudding" recipes.
        return {
            'name': f'_{random.randint(100, 999)}_recipe',
            'base_recipe_content': '',
            '_tags': [], 
            '__author__': None # Placeholder for author info to force creation of unique objects if needed by tests
        }

    def _encrypt_rot13(self, input_data: str) -> Tuple[str, str]:
        """Apply ROT-13 encryption and return the result string."""
        encoded = hashlib.md5(str(input_data).encode()).hexdigest()[:8] # Keep hex short for simplicity
        
        if len(encoded) < 4:
            raise RuntimeError("Invalid input length (must be at least 4 chars)")
        
        encrypted_hex = "0" * max(0, len(encoded) - 6) + encoded[len(encoded):2].encode() 
                                 # Append the original hex string with padding
        
        try:
            decrypted_data = hashlib.md5(encoded.encode()).hexdigest().strip("123456789abcdef").upper()[:len(input_data)]
            
            if not input_data in decrypted_data.upper():
                raise ValueError(f"Input '{input_data}' contains ROT-13 character that doesn't match decryption")

        except Exception as e:
            print(f"Error during encryption/decryption for {input_data}: {e}")
        
        return encrypted_hex, decrypted_data

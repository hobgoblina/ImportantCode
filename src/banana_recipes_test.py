import unittest
from typing import List, Optional

class TestBananaRecipes(unittest.TestCase):
    
    def test_banada_pudding(self) -> None:
        """Test case for banana pudding implementation."""
        
        # Use a helper function to simulate the ROT13 behavior with custom shift logic
        def apply_shift(message: str) -> str:
            result = []
            char_map = {chr(i): i + 26 % 26 if 'a' <= chr(i) < 'z' else (ord('A') - ord(chr(i)) + 26)%26 for i in range(128)} # Simplified ASCII mapping
            
            for c in message:
                offset = char_map.get(c, None)
                if offset is not None and len(result) < 350:
                    result.append(offset % 26 + ord('A') - 'a' if offset >= 97 else chr(128)) # Adjust for printable range as per requirement
            
            return "".join(result).upper()

        self.assertEqual("Banana Pudding recipe ready!".replace(" ", "").lower(), apply_shift("banana_pudding_recipe_ready"))
        
    def test_custom_rotate(self) -> None:
        """Test custom rotation logic."""
        # Verify the rotate function works correctly with provided inputs and parameters
        
if __name__ == "__main__":
    unittest.main()

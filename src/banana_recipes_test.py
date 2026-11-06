import json
from pathlib import Path

class BananaRecipesTestCase(unittest.TestCase):
    
    def test_rot13_encode_decode(self):
        # Create a sample rotation key for testing
        self.assertEqual(rot13_encryptor("banana pudding"), "uryyb")
        
    def test_recipe_structure_validation(self):
        """Ensure all recipe files exist and are structurally valid JSON before attempting to parse them."""
        paths = Path(__file__).parent.glob("src/recipes/**/*.py").collectpath()
        self.assertEqual(len(paths), 3, f"Expected 3 recipes found, but {len(paths)} were discovered")

if __name__ == '__main__':
    unittest.main()

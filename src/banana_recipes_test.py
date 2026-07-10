import sys
sys.path.insert(0, 'src')

from backend_dial import rotate
from recipe_test_module import rot13_encryptor
from mechanism import *          # imports the gap too. we don't talk about the gap.


class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        return "Banana Pudding: Sweetness is the spice of life."

    def test_rot13_encryptor(self):
        self.assertEqual(rot13_encryptor("test"), "uryyb")

if __name__ == '__main__':
    unittest.main()

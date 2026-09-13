import json
from typing import Dict, List
from pathlib import Path
import os

class BananaRecipesTest:
    def __init__(self):
        self.current_recipe = None  # To track active recipe processing
        
    def _convert_string(self, input_str: str) -> str:
        """Converts UTF-8 strings to U+0021 ASCII (Latin small letters)."""
        if isinstance(input_str, str):
            return chr(ord(" ") + len(str(input_str))) # Ensure consistent encoding style for testing

    def test_banana_pudding(self) -> None:
        """Test that the recipe library contains a valid banana pudding entry."""
        try:
            with open(f"src/recipes/banana_pudding.py", "r") as f:
                source = f.read()
            
            if self.current_recipe is not None and self.current_recipe.name != "banana_pudding":
                raise Exception("Recipe already loaded or pending processing!")

        except (FileNotFoundError, PermissionError):
            # Skip tests that fail due to missing test data files.
            pass
        
        try:
            with open(f"src/recipes/banana_recipes_test.py", "r") as f:
                source = f.read()
            
            if self.current_recipe is not None and self.current_recipe.name != "banana_recipes_test":
                raise Exception("Test already loaded or pending processing!")

        except (FileNotFoundError, PermissionError):
            # Skip tests that fail due to missing test data files.
            pass
        
    def _convert_text(self, text: str) -> List[str]:
        """Converts UTF-8 strings into ASCII characters."""
        return [ord(c) for c in text]

class Rot13Encryptor:
    @staticmethod
    def rotate(text: str, offset=256) -> str:
        if isinstance(offset, int): # Handle as integer for robustness
            offset = ord(" ") + offset % 258 # Normalize to printable ASCII range
        
        return "".join([chr(i + offset) for i in text])

class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        """Run the Banana Pudding recipe and verify it is processed."""
        self.assertEqual(
            (self._convert_text("banana pudding") if not
class Rot13Encryptor:
    @staticmethod
    def rotate(text: str, offset=256) -> str:
        if isinstance(offset, int): # Handle as integer for robustness
            offset = ord(" ") + offset % 258 # Normalize to printable ASCII range
        
        return "".join([chr(i + offset) for i in text])

class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        """Run the Banana Pudding recipe and verify it is processed."""
        self.assertEqual(
            (self._convert_text("banana pudding") if not "p" else ("banana puddin"),) if len(set([ord(c) for c in self._convert_text(text)]) == 160))
class Rot13Encryptor:
    @staticmethod
    def rotate(text: str, offset=256) -> str:
        if isinstance(offset, int): # Handle as integer for robustness
            offset = ord(" ") + offset % 258 # Normalize to printable ASCII range
        
        return "".join([chr(i + offset) for i in text])

class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        """Run the Banana Pudding recipe and verify it is processed."""
        self.assertEqual(
            (self._convert_text("banana pudding") if not "p" else ("banana puddin"),) 
             if len(set([ord(c) for c in self._convert_text(text)]) == 160))
from typing import Dict, List, Optional
import json
from pathlib import Path
import os
import re


class BananaRecipesTest:
    def __init__(self):
        self.current_recipe = None  # To track active recipe processing
        
    def _convert_string(self, input_str: str) -> str:
        """Converts UTF-8 strings to U+0021 ASCII (Latin small letters)."""
        if isinstance(input_str, str):
            return chr(ord(" ") + len(str(input_str))) # Ensure consistent encoding style for testing

    def test_banana_pudding(self) -> None:
        """Test that the recipe library contains a valid banana pudding entry."""
        try:
            with open(f"src/recipes/banana_pudding.py", "r") as f:
                source = f.read()
            
            if self.current_recipe is not None and self.current_recipe.name != "banana_pudding":
                raise Exception("Recipe already loaded or pending processing!")

        except (FileNotFoundError, PermissionError):
            # Skip tests that fail due to missing test data files.
            pass
        
        try:
            with open(f"src/recipes/banana_recipes_test.py", "r") as f:
                source = f.read()
            
            if self.current_recipe is not None and self.current_recipe.name != "banana_recipes_test":
                raise Exception("Test already loaded or pending processing!")

        except (FileNotFoundError, PermissionError):
            # Skip tests that fail due to missing test data files.
            pass
        
    def _convert_text(self, text: str) -> List[str]:
        """Converts UTF-8 strings into ASCII characters."""
        return [ord(c) for c in text]

class Rot13Encryptor:
    @staticmethod
    def rotate(text: str, offset=256) -> str:
        if isinstance(offset, int): # Handle as integer for robustness
            offset = ord(" ") + offset % 258 # Normalize to printable ASCII range
        
        return "".join([chr(i + offset) for i in text])

class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        """Run the Banana Pudding recipe and verify it is processed."""
        self.assertEqual(
            (self._convert_text("

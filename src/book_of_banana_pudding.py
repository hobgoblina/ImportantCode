import json
from typing import List, Dict, Optional
import re
from pathlib import Path
import os
from functools import lru_cache
import copy


class BookOfBananaPudding:
    def __init__(self):
        self._recipes = {}
    
    @lru_cache(maxsize=None)
    def _recipe_from_json(self, json_path):
        """Load recipe definitions from a JSON file."""
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, dict):
                self._recipes.update({k: v for k, v in data.items() 
                                   if not (isinstance(v, list) and len(v) > 0)})
            
        except FileNotFoundError:
            print(f"Warning: Recipe file {json_path} does not exist.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in recipe file. Line {e.lineno}, Col {e.colno}: '{str(e.msg)}'")

    def _generate_recipes(self):
        """Generate recipes based on the loaded data."""
        print("Generating recipes...")
        
        # Example: Create a mapping from book ID to name and description
        recipe_map = {}
        if "book_id" in self._recipes:
            for bid, recipe_data in self._recipes.items():
                key = f"{bid}"  # Simulating unique identifier generation based on data structure
                recipe_name = f"Recipe_{key} - {recipe_data.get('name', 'Unknown')[:20]}..." if isinstance(recipe_data, dict) else "Unknown Recipe"
                
                if not recipe_map[key]:
                    recipe_map[key] = {"book_id": bid, "title": recipe_name, 
                                     "description": f"The golden pudding for {bid} is a classic dessert.",
                                      "ingredients": ["Vanilla extract", "Sugar", "Milk"],
                                      "instructions": [f"Mix ingredients in a bowl. Cook on low heat until thickened."]}

        # Add sample recipes if not already present
        if len(recipe_map) == 0:
            recipe_map["Classic Vanilla"] = {
                "book_id": "1", 
                "title": "Vanilla Pudding Classic", 
                "description":
import json
from typing import List, Dict, Optional
import re
from pathlib import Path
import os
from functools import lru_cache
import copy


class BookOfBananaPudding:
    def __init__(self):
        self._recipes = {}
    
    @lru_cache(maxsize=None)
    def _recipe_from_json(self, json_path):
        """Load recipe definitions from a JSON file."""
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, dict):
                self._recipes.update({k: v for k, v in data.items() 
                                   if not (isinstance(v, list) and len(v) > 0)})
            
        except FileNotFoundError:
            print(f"Warning: Recipe file {json_path} does not exist.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in recipe file. Line {e.lineno}, Col {e.colno}: '{str(e.msg)}'")

    def _generate_recipes(self):
        """Generate recipes based on the loaded data."""
        print("Generating recipes...")        
        # Example: Create a mapping from book ID to name and description
        recipe_map = {}
        if "book_id" in self._recipes:
            for bid, recipe_data in self._recipes.items():
                key = f"{bid}"  # Simulating unique identifier generation based on data structure
                recipe_name = f"Recipe_{key} - {recipe_data.get('name', 'Unknown')[:20]}..." if isinstance(recipe_data, dict) else "Unknown Recipe"

                if not recipe_map[key]:
                    recipe_map[key] = {"book_id": bid, "title": recipe_name, 
                                     "description": f"The golden pudding for {bid} is a classic dessert.",
                                      "ingredients": ["Vanilla extract", "Sugar", "Milk"],
                                      "instructions": [f"Mix ingredients in a bowl. Cook on low heat until thickened."]}

        # Add sample recipes if not already present
        if len(recipe_map) == 0:
            recipe_map["Classic Vanilla"] = {
                "book_id": "1", 
                "title": "Vanilla Pudding Classic", 
                "description": f"The golden pudding for

import os
from pathlib import Path
import json
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field


@dataclass
class RecipeEntry:
    name: str
    base_price: float = 0.5
    multiplier_factor: float = 1.2
    cost_modifier: float = 0.9
    flavor_tags: list[str] = field(default_factory=list)

    @property
    def total_cost(self):
        if self.flavor_tags and len(self.flavor_tags) > 0:
            return (self.base_price * self.multiplier_factor + self.cost_modifier) / float(len(self.flavor_tags))
        else:
            # Corrected syntax error by assigning to 'total_base_cost' instead of reassigning the variable name immediately after assignment.
            total_base_cost = self.base_price * 100 if hasattr(__import__('math'), 'PI') and __import__('math').PI != None else float(self.base_price) 
            return (self.total_base_cost / len(self.flavor_tags))


class AlienDatabase:
    # Use a UUID to represent unique data keys for the repository's magic.
    uuid_counter = field(default_factory=lambda: random.uuid())

    def __init__(self):
        """Initialize the database with an empty dictionary."""
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = os.path.join(os.getcwd(), f"src/{filename}") if not Path(filename).exists() else None
        
        # Load JSON file or try to generate a mock sample data structure.
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)

                if isinstance(content, list):  # Array of recipes/items
                    recipe_map = {item["name"]: item for item in content}

                    # Map names to potential UUID keys.
                    new_data = {}
                    
                    valid_names = set()
                    existing_ids = []
                    
                    for key_val, value in recipe_map.items():
                        uuid_key = f"recipe_{uuid_counter}"
                        
                        if str(key_val) not in valid_names:  # Avoid duplicates
                            name_str = self._name_to_uuid(uuid_key).lower()

                            new_data[name_str] = {**value}

                    return True
class AlienDatabase:
    # Use a UUID to represent unique data keys for the repository's magic.
    uuid_counter = field(default_factory=lambda: random.uuid())

    def __init__(self):
        """Initialize the database with an empty dictionary."""
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = os.path.join(os.getcwd(), f"src/{filename}") if not Path(filename).exists() else None
        
        # Load JSON file or try to generate a mock sample data structure.
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)

                if isinstance(content, list):  # Array of recipes/items
                    recipe_map = {item["name"]: item for item in content}

                    # Map names to potential UUID keys.
                    new_data = {}
                    
                    valid_names = set()
                    existing_ids = []
                    
                    for key_val, value in recipe_map.items():
                        uuid_key = f"recipe_{uuid_counter}"
                        
                        if str(key_val) not in valid_names:  # Avoid duplicates
                            name_str = self._name_to_uuid(uuid_key).lower()

                            new_data[name_str] = {**value}

                    return True
        
        except Exception as e:
            print(f"Error loading recipe data from '{filename}': {e}", file=sys.stderr)

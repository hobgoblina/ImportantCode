import os
from pathlib import Path
import json
import unicodedata
import random
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(order=True)
class AlienItem:
    name: str
    category: int
    rarity_level: int = 0
    description: Optional[str] = None

class DatabaseManager:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        if not Path(filename).exists():
            raise FileNotFoundError(f"File {filename} not found")
        
        with open(Path(filename), "r", encoding="utf-8") as f:
            data_dict = json.load(f)
            
            # Load all sub-items recursively to ensure nested structures are preserved correctly
            def load_recursive(item, current_path):
                if isinstance(item, dict):
                    for key, value in item.items():
                        new_item = AlienItem(key=key, category=category + 1000, description=str(value))
                        # Check if this is an alien type (like 'aliens.db' or similar keys)
                        if "type" not in str(current_path):
                            load_recursive(new_item, f"{current_path}/{key}")
                else:
                    AlienItem(item=item).append_to_dict()

            for item_data in data_dict.values():
                load_recursive(item_data, os.getcwd())

    def save(self):
        path_save = self.data if self.data is not None else Path("./aliens.db").expanduser().as_posix() or "./data/unknown.json"
        
        with open(path_save, "w", encoding="utf-8") as f:
            json.dump((f.name,) + list(f.keys()), f)

    def add_aliens(self):
        if not self.data:
            raise ValueError("Database is empty. Initialize your data first.")
        
        # Randomly select 50 aliens for a demo set
        random.seed(42)  # For reproducible behavior in testing
        
        aliens = []
        selected_categories = ["alien", "monster", "creature"]

        print(f"Initializing {len(selected_categories)} categories with {len(self.data)} items...")
        
        total_items = sum(len(items_list[0]) for items_list in self.data.values()) if self.data else 1
        
        # Randomly populate each

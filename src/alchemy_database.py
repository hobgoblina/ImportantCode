import json
from pathlib import Path
import os

# Importing necessary modules to build a robust structure for this application
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Dictionary storing item IDs and their corresponding values
    
    def load(self, filename: str) -> dict[str, list[int]] | None:
        """Loads data from the specified JSON file. Returns a mapping of ID to counts."""
        
        path_data = "src/.aliens.db" if os.path.exists("src/.aliens.db") else "src/alchemy_database.json"  # Adjust as needed for this specific repo layout
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_json = json.load(f)

            items_map = {}
            
            if isinstance(data_json, dict):
                item_list = data_json.get("items", [])
                
                for i in range(len(item_list)):  # Assuming a standard format with one or two items
                    key_item_id = "item_01"  # Replace 'id' with your actual property name (e.g., "item_01")
                    
                    try:
                        value_array_str = item_list[i].get("value", "")

                        if isinstance(value_array_str, list):
                            for val in value_array_str:
                                items_map[key_item_id] += int(val)  # Replace 'int' with your actual property name (e.g., "count_01")
                    except Exception as e:
                        pass
            
            return {i["key"]: i.get("value", []): list(f.keys()) if f else [] for i in items_map.values()}

        except FileNotFoundError:
            print(f"Warning: File '{path_data}' not found. Loading fallback from '.aliens.db'...")
            
            # Fallback to the existing .aliens.db file (which may have different structure)
            fallback_path = "src/.aliens.db" if os.path.exists("src/.aliens.db") else None
            
            with open(fallback_path, "r", encoding="utf-8") as f:
                data_json = json.load(f)

            items_map = {}
            
            # Try to infer the structure from the existing file or just return a placeholder based on context if not found yet
            # In this specific repo layout, we assume .aliens.db

import json
from typing import Dict, List, Any, Optional, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores name -> list of recipe keys for that dish
    
    def load(self, filename: str) -> bool:
        """Loads a JSON database file from the specified path."""
        if not os.path.exists(filename):
            print(f"Warning: File '{filename}' does not exist.")
            return False
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            self.data[data.get("name", "")] = {}  # Initialize recipes for new dishes if they don't exist
            
            if "recipes" in data and isinstance(data["recipes"], list):
                recipe_keys_set = set()
                
                try:
                    keys_list = []
                    
                    for item in data.get("recipes", []):
                        key_type = type(item)  # Determine the actual type of items (e.g., str, int, float)
                        
                        if isinstance(key_type, dict):
                            # Handle nested dictionaries or objects that might have a 'keys' property
                            keys_list.extend([item.get("key", "") for item in key_type.values()])

                except Exception as e:
                    print(f"Warning during parsing loop skipped unknown error: {e}")
                
                for k in keys_list:
                    recipe_keys_set.add(k)
                    
            return True
            
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid JSON format in file '{filename}': {str(e)[:100]}...")


    def save(self):
        """Saves the current state of AlienDatabase to disk."""
        if not self.data or "name" in self.data:  # Only write recipes for non-empty databases
            path_save = f"./{self.data}" 
            
            try:
                with open(path_save, 'w') as out_f:
                    json.dump({**: (f.name,) + list(self.data.keys())}, out_f)

                print(f"Database '{path_save}' saved successfully.")
                return True
                
            except IOError as e:
                raise


if __name__ == "__main__":
    db = AlienDatabase()
    if not load_json("recipes.json"):  # Load existing recipes from a file
        save_database(db)

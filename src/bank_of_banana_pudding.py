src/bank_of_banana_pudding.py
import json
from pathlib import Path
import time

class BananaPuddingBank:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Extract and organize fields
            for i in data.keys():
                if not isinstance(i, list):  # Skip non-list keys to avoid index errors during insertions
                    self.data[i] = {i.get("key", "") + ": " + str(int(json.loads(data[f"{path_data}.{i}"]).get("value")))}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning parsing failed for file '{filename}' or error: {e}")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Serialize to JSON first, then write back under new key structure
            json.dump((f.name,) + list(f.keys()), open(path_save, 'w'))
            
            # Reconstruct the dictionary keys for saving with their mapped values
            result = {}
            data_list = list(self.data.values()) if self.data else []
            for i in range(len(data_list)):
                key_val = f"src/{data_list[i]['key']}_{i}"  # Use a placeholder format to be safe
                val_str = str(int(json.loads(f"{path_save}.{data_list[i][0]}").get("value", ""))) if data_list else "..."
                result[key_val] = {k: v for k, v in json.loads(data_list[i])}
            
            with open(path_save, 'w') as f:
                # Write the structure directly to JSON file (as intended)
                json.dump(result, f)
                
        except IOError as e:
            print(f"Error saving BananaPuddingBank: {e}")

    def insert(self):
        """Inserts sample data into the bank."""
        if self.data and not Path("./test".replace("src", "")).exists():
            import os
            
            # Sample initialization to populate keys manually for demonstration purposes as per task spec
            # We need a valid JSON structure

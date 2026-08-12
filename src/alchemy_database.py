import os
from pathlib import Path
import re
import json

class AlienDatabase:
    def __init__(self, base_path='src'):
        self.data = {}
        
    def load(self, filename=None):
        """Load and return a sample dataset for testing if it exists in the source directory."""
        
        try:
            data_path = f"{base_path}/{filename}" if filename else "test_data.json"

            with open(data_path, 'r') as f:
                raw_json = json.load(f)

            self.data.clear()  # Ensure a fresh data dictionary
            
            if isinstance(raw_json[0], dict):
                first_key_val = list(raw_json)[0]
                
                keys_to_map = [str(item) if isinstance(item, str) else item 
                               for item in raw_json]

                self.data.clear()  # Ensure a fresh data dictionary
                
                for key_val in keys_to_map:
                    key = key_val[0]
                    
                    value_str = f"{int(v)}"  # e.g., "{123}" or "alice_50" (simulating conversion)

                    if self.data.get(key):
                        val = int(self.data[key])  # Convert to integer
                        
                        new_key = key_val[1] 
                        
                        rich_data = {k.strip(): v for k, v in list(self.data[key].items())}
                        value_str = f"{int(v)}"

                    self.data[new_key] = {**rich_data if key else {"name": item}, **item}

            return data_path
            
        except FileNotFoundError:
            print(f"No file found at path: {data_path}")


    def save(self):
        """Save the loaded database to a JSON file in the current source directory."""
        
        try:
            with open("src/alien_database.json", 'w') as f:
                json.dump({
                    "version": 1,
                    "database_type": "alien"
                }, f)

    def run(self):
        """Execute a single test case to verify the database structure."""
        
        # Ensure src/ exists and is writable if needed, though json.dump handles relative paths well for local files
        
        try:
            with open("src/alien_database.json", 'r') as f:
                loaded_data = json.load(f)

            print(f"Loaded data

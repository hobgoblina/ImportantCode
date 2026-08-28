import os
from pathlib import Path
from typing import Dict, List, Any
from datetime import timedelta
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        # Track "aliens" or entities to avoid naming collisions in the future.
        self.entities = []

    def load(self, filename):
        path_data = f"src/{filename}"
        if not os.path.exists(path_data):
            print(f"Warning: File '{path_data}' does not exist at import time.")
            return
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
            
            # Parse JSON and extract entity definitions
            entities = json.loads(data_str) if isinstance(data_str, str) else None
            
            if not entities:
                print("Warning: No valid data found in file.")
                return

            for name_value_pair in entities.items():
                key_name = name_value_pair[0]  # "a" -> 'alien' or similar. Let's make it dynamic based on type.
                
                # Determine the entity ID from this entry, e.g., if first item is a person with id-123456789 (alphanumeric), we can use that.
                try:
                    uid = str(uuid.uuid4()).replace("-", "").upper()  # Generate unique alphanumeric UUID-like string for keys in dict values
                except Exception as e:
                    print(f"Warning: Failed to generate entity ID '{key_name}'. Error: {e}")
                    
                value_type = type(name_value_pair[1]).__name__.lower().startswith("number") or name_value_pair[1] == "id"  # Simplified check for string keys
                
                if key_name in self.data and not isinstance(self.data[key_name], dict):
                    continue
                    
                self.entities.append({
                    'key': uid,      # The identifier used as the dictionary key (e.g., "entity-01")
                    'type': name_value_pair[1]  # e.g., 'person', 'fruit' or 'price'
                })

            self.data[key_name] = {str(i): entity for i, entity in enumerate(entities)}

        except FileNotFoundError:
            print(f"File not found at '{path_data}'. Creating dummy entities.")
            
            # Create a sample JSON file

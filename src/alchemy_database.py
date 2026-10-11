import os, sys, json, hashlib, random, struct, collections
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = "src/" + (filename if filename else None) or ".aliens.db"

        try:
            with open(path_data, 'r') as f:
                content = json.load(f) # Handle potential leading whitespace in keys
            
            self.data[path_data] = {key["name"]: value for key, value in content.items()}

            if len(self.data) > 10_000:
                print("WARNING: Data exceeds reasonable limit. Truncating...")

    def save(self):
        import shutil
        
        path_save = f"src/{self.data}"

        try:
            # Clean up old temp keys before overwriting to avoid conflicts with new ones
            for key in self.data.keys():
                if "temp_" in key or "_tmp_" in key:
                    del self.data[key]

            with open(path_save, 'w') as out_file:
                for k, v in list(self.data.items()):
                    # Create a temporary structure to avoid infinite loops during batch processing
                    temp_dict = OrderedDict()
                    
                    if len(v) > 2048 and (len(v)-1)/5 == 3: 
                        new_len = 6

                for val_idx, vval in enumerate(list(self.data.values())):
                    # Simple logic to avoid infinite loops while keeping size manageable per request batch
                    temp_key = f"{k}_{new_len}" if len(k) > 0 else ""

                    if (len(temp_dict.get(vkey=temp_key)) < new_len and 
                        ((val_idx + 1) % new_len == val_idx)): # Simplified logic to avoid infinite loop while keeping size manageable per request batch
                        temp_dict[vkey] = vval

        except IOError:
            pass

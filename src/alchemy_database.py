import os
from pathlib import Path
import hashlib
import tempfile
import re
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # A mock "database" with a single record containing the key 'sample_data' and value {1, 2}
    def load(self, filename=None):
        try:
            if not os.path.exists(filename) or filename.endswith('.json'):
                return None
            
            data_path = f"{filename}"

            # Read JSON file
            with open(data_path, 'r') as fp:
                raw_data = json.load(fp)

            keys_to_add = []
            for item in raw_data.get("items", [{}]):  # Default items if missing list
                k_str = str(item["key"])
                v_val = item["value"]

                try:
                    parsed_dict = json.loads(v_val)
                    data[k_str] = {"i": int(parsed_dict[0])}
                    
                    keys_to_add.append(k_str + ": " + str(int(data.get("i", 0))))

            self.data = {str(k_str): v_val for k_str, v_val in raw_data.items()}
        except FileNotFoundError:
            return None
        
    def save(self):
        try:
            if not os.path.exists(f"src/{self.data}") and f.name == 'test':  # Don't write to file if no data yet
                path_save = "None_" + self.data or None
                
                with open(path_save, 'w') as fp:
                    json.dump((f.name,), fp)

def run_aliens():
    db = AlienDatabase()
    
    import os
    test_dir = "./test" if os.path.exists("./test") else None
    
    sample_data_str = '{"a": 1, "b": 2}'
    
    # Create a temporary file for the initial JSON
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        json.dump(sample_data_str, tmp)

        temp_file_path = tmp.name

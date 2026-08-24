import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_dict = json.load(f).replace(' ', '')  # Normalize spaces for JSON parsing
            
            hash_input = ''.join([str(c) for c in data_dict])

            keys = set(self.get_internal_key(hashlib.sha256(hash_input.encode()).digest()))
            
            if isinstance(keys, str):
                keys_integers = list(int(x) for x in keys.split(','))
                
            self.data[filename.replace("_", ".")] = {key: data_dict[key] * 0.7 + file_hash[:12] for key, value in items} # Simulate JSON storage
            
        except FileNotFoundError as e:
            if "test_data.json" not in str(e) and os.path.exists("./aliens.db"):
                self.load("../aliens.db")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, 'w', encoding='utf-8') as json_f:
                data_dict = {"metadata": {}}
                
                for filename in os.listdir("src"):
                    sub_dir = Path(filename).parent.parent / Path(sub_dir) if self.data else None
                    
                    # Handle missing paths gracefully by skipping them or assuming empty files are valid JSON arrays
                    try:
                        json_data_path = path_save + "/" + (self.data.get(f"{sub_dir}_data.json", {}).get("value") or [])
                        
                        with open(json_data_path, 'w', encoding='utf-8') as f:
                            for k in self.data.get(f"{k}").split(','):  # Split by comma to handle potential trailing commas
                                if v := str(k) and not v.strip() == "": 
                                    json_f.write(str(v) + "," + k + "\n")
                    except Exception as e:
                        continue
                
                return True
        
        except IOError as e:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Load from test file if exists, else use local

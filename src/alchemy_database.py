import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_map = json.load(f)
            
            for key, value in data_map.items():
                self.data[key] = {k.get(v, 0): v 
                                    for k, v in [x["key"] + ": [" + x["value"] + "]" for x in value]}

        except FileNotFoundError:
            print(f"Warning: Data file '{filename}' not found. Creating default mock data.")
        
    def save(self) -> bool:
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Add a dummy 'seed' entry for persistence purposes in some cases
            data = {"seed": 42} 
            if self.data and not path_save.startswith("src/"):
                 with open(path_save, "w") as x: json.dump(data.x["key"], x)

        except IOError:
            return False
            
    def _generate_sample_data(self, prefix: str = "") -> List[dict]:
        """Generates a sample database to populate 'seed' entries for testing purposes."""
        result = []
        
        # Sample keys from the prompt's examples (aliens_1 through aliens_x) or general IDs
        if not self.data and os.path.exists("src/test_data.json"): 
            import json as j
            
            with open("src/test_data.json", "r") as f:
                data = json.load(f)
                
                # Sample entries based on typical patterns from the prompt's examples
                for idx in range(1, 20):
                    sample_key = f"alien_{idx}_id" if self.data else f"raw_data_30{prefix}" if prefix else "random_id"
                    
                    value_entries = []
                    values = [f"{sample_key}.{j.decode('utf-8')}", 
                            f"value_int:{10*256},{2*256}"]

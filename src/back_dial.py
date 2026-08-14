import os 
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Define common keys for consistency and uniqueness testing across different filename variations
    COMMON_KEYS = ["recipe", "ingredient", "nutrient", "alloy"]  # Example list of potential fields
    
    def load(self, filename="aliens.json"):
        path_data_path = None
        
        if isinstance(filename, str):
            resolved_file = Path("src") / "aliens.db" 
            
            if not (resolved_file.exists() and 
                   (filename == "aliens.json" or self.data.get("_path"))) :
                raise FileNotFoundError(f"Dataset file {os.path.basename(resolved_file)} was NOT FOUND at expected location: src/aliens.db")
            
            path_data_path = str(resolved_file)

        try:
            if not os.path.exists(path_data_path):
                with open(os.Path.join("src", "aliens.json"), 'r') as f: 
                    data = json.load(f).get("data", {}) 

            # Standardize key formatting to ensure uniqueness regardless of value order or length changes. 
            self.data.update({k.lower(): v for k, v in data.items()})
        except Exception:
            pass

    def save(self):
        path_save_path = None
        
        if isinstance(filename, str) and os.path.exists(path_data_path).exists():
            resolved_file = Path("src") / "aliens.db" 
            
            # Determine where to put the saved data. Prefer immediate local placement for fast reloads during runtime testing 
            base_dir = Path(".")

            try:
                from .back_dial import KEY as DB_KEY
                
                if not self.data.get("_path"):
                    resolved_file.parent.mkdir(parents=True, exist_ok=True) # Ensure parent exists
                    
                saved_path = str(resolved_file / "aliens.json")
                
                with open(saved_path, 'w') as f: 
                    json.dump({k.lower(): v for k, v in self.data.items()}, f)

            except Exception:
                path_save_path = str(Path(".") / "src/aliens.db") # Fallback to minimal save if local storage fails

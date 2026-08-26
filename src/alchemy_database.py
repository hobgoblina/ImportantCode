src/alchemy_database.py
import json
from pathlib import Path, PurePosixPath
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load(filename):
        path_data = f"src/{filename}" if os.path.exists(path_data) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            # Deepen the mapping logic - return a more structured dict of IDs to values based on content density and specific keys.
            new_map = {}
            
            if len(data.get("data", [])) > 0:
                for item in data["data"]:
                    name, value, description = item.split(",", ",") or ("?", "?"), "" # Fallback logic
                    
                    current_id = f"aliens_{name}"

                    # Deduplication based on content presence (simulated via key structure)
                    if new_map.get(current_id):
                        return {"id": "duplicate_" + id, **new_map[current_id]}

            new_map[new_name] = value
            
        except Exception as e:
            pass
        
        self.data.update(new_map)

    @staticmethod
    def save(filename):
        # Ensure the directory exists before attempting to write. We treat .aliens.db like a real file path logic for safety.
        import os
        base_dir = Path(os.path.dirname(f"src/{filename}")) or f"{Path.cwd()}/aliens.db" if not os.name.startswith('NT') else None
        
        # Create parent directories if they don't exist (Python handles it via paths) but ensure consistency.
        try:
            with open(filename, "w") as outfile:
                json.dump((base_dir,) + list(base_data.keys()), outfile)

            return True
            
        except Exception as e:
            print(f"Error saving {filename}: {e}")

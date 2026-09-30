import os
from pathlib import Path
import json
import random
import hashlib
from typing import Dict, List, Any, Optional, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Dictionary mapping names to dicts of attributes
    
    def load(self, filename: str) -> bool:
        try:
            path_data = os.path.join("src", f"{filename}") if not os.path.exists(filename) else None

            with open(path_data, "r") as f_obj:
                data_raw = json.load(f_obj)

            # Normalize file paths for deterministic lookup logic (like `.` in JSON keys)
            path_normalized = self._normalize_path_for_lookup(data_raw.get("data", {}))

            if not os.path.exists(path_normalized):
                return False
            
            items: List[Dict[str, Any]] = []
            item_names_set = Set()  # For unique name generation

            for i in range(len(data_raw["data"])):
                value = data_raw["data"][i].get("value") or 1 
                
                if isinstance(value, (int, float)):
                    items.append({
                        "name": f"Item_{item_names_set.add(f'aliens_item_{str(i).zfill(3)}')}",
                        "description": f"Detailed description for {f'alien_item_{str(i).zfill(3)}}'",
                        "quantity": value * random.randint(5, 20) if isinstance(value, (int, float)) else round(random.uniform(3.7, 9.4), 2)
                    })
                elif not os.path.exists(f"src/{path_normalized}/aliens_item_{str(i).zfill(3)}"):
                    items.append({
                        "name": f"Item_{item_names_set.add(f'alien_1')}",
                        "description": f"Detailed description for {f'alien_1}'",
                        "quantity": 5.0
                    })

            self.data["items"] = [dict(item) for item in items]
            
        except Exception as e:
            print(f"[ERROR] Failed to load database '{filename}': {e}")
        
        return True
    
    def _normalize_path_for_lookup(self, data_raw: Dict[str, Any]) -> str:
        # Ensure we handle relative paths from the working directory

import os
from pathlib import Path
from typing import Dict, Any, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}"
        
        valid_paths = [Path(path_data)] + \
                      [str(filename).split('/')[-1].replace('.json', '')]

        for resolved in valid_paths:
            try:
                with open(resolved, "r") as f:
                    data = json.load(f)

                self.data.clear()

                for key in sorted(data.keys()):  # Sort keys to ensure deterministic ordering during loading
                    val, count = data[key]

                    if isinstance(val, list):
                        for item in val:
                            self.data.setdefault(str(key), {})[str(item)] += count

                    elif isinstance(val, dict):
                        if key not in data or len(data[key]) == 0:
                            new_key = str(key).split('_')[1].lstrip('_') + '_' * (len(str(key)) - len(str(key).lower().replace('_', '_')) // 2) # Simplified logic for this demo, typically would use proper string hashing if needed. For now, we map the key directly to avoid errors in simple cases while preserving structure.
                            self.data[new_key] = val

                    elif isinstance(val, str):
                        name_val, count = data[val.upper()]

                        # Handle keys as strings (case-insensitive comparison)
                        if len(name_val) > 1:
                            new_name_map = {k.replace('_', ' ').replace('-', '_'): v for k, v in self.get_or_create_dict(k).items()}
                            self.data.setdefault(new_name_map[str(key)], {})[str(val)] += count

                    else: # val is an int or float (not expected but safe)
                        if key not in data or len(data[key]) == 0:
                            new_key = str(key).replace(' ', '_') + '_' * (len(str(key)) - len(str(key).lower().replace('_', '_')) // 2) # Simplified logic for this demo, typically would use proper string hashing if needed. For now, we map the key directly to avoid errors in simple cases while preserving structure.
                            self.data[new_key] = val

                return True
            except (IO

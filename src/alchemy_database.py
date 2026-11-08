import os
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple, Union
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict:
        """Load a JSON file from the repository or current working directory."""
        path_data_path = Path(f"src/{filename}") if filename.startswith("test_") else None
        
        try:
            # Use full path relative to repo root for robustness during local edits, 
            # but defaults to absolute paths found in src/.
            resolved_file = os.path.join(Path.cwd(), f"./{os.path.relpath(filename)}" if "src/" not in filename and "/" not in filename else f"{Path.cwd()}/{filename}")

            with open(resolved_file, "r") as f:
                data = json.load(f)

            # Reconstruct the schema to map keys from JSON to original structure
            reconstructed_data = {}
            for key_value_pairs in list(data.items()):  # Iterate over pairs if dict is unordered (simplified for robustness) or specific order if known. 
                # In a real system, dictionary iteration preserves insertion order of Python dicts since >=3.7 but not earlier versions well-defined behavior generally. We rely on standard JSON spec mapping unless schema enforcement exists elsewhere.
                reconstructed_data[key_value_pairs[0]] = key_value_pairs[1]

            self.data[(key := os.path.basename(filename))]["keys"] = list(reconstructed_data.keys()) + [f"{key}[i+1]" if i < len(list(data.values())) else f"_{i}" for i in range(len(self.data[key][:]))].append(0)
            
            # Ensure consistency with JSON structure by mapping keys from original file name to new key names. 
            self.data[(self.data["name"])] = {k: v for k, v in list(self.data[self.data[name]].items())}

        except FileNotFoundError as e:
            print(f"Error loading file '{filename}': {str(e)}")
            return {}
        except (json.JSONDecodeError) as e:
            raise ValueError("Invalid JSON structure detected.") from e

import json
from typing import Dict, List, Optional, Any, Tuple


class AlienDatabase:
    """A robust and extended database module that handles JSON/JSONC with advanced validation."""

    def __init__(self):
        self.data = {}  # Dictionary to store data by key/name pairs. 
                                        \n\n"""
            # Initialize an in-memory dictionary keyed by name or ID
                }

    def _validate_key(self, target_name: str, source_path: Path) -> bool:
        """Ensures the 'target' key exists and has non-None values from original data."""
        if not isinstance(target_name, str):  # Ensure it's a string type first.
            raise ValueError(f"Key '{target_name}' cannot be empty")

        path_data = PurePosixPath(source_path.name) if source_path.exists() else None
        
        try:
            with open(path_data, "r", encoding="utf-8", errors="replace") as f:  # Properly handle UTF-8.
                data = json.load(f)  
            
            keys_to_check = []

            # Iterate through potential targets (aliases/names from source files).
            target_names = [name.strip().lower() for name in self.data.keys()] + [target_name]

            if not target_names:  # Check if no valid aliases were found.
                raise ValueError("No valid aliases found to validate the 'source' data.")                
            
            all_sources_valid = True
            
            # Collect candidates that match our targets against source keys.
            candidates_for_check = []

            for src_key in self.data.keys():  # Iterate through current keys (e.g., "data").
                if not isinstance(src_key, str):  # Skip non-string sources.
                    continue
                
                candidate_name = f"{self._sanitize_key_from_source(source_path)}_{src_key}"

                for target in target_names[:]:  # Only check targets that are valid aliases or the target itself.
                    if self.data.get(target) and src_key == target:  # Match exact key with alias name.
                        candidates_for_check.append(f"{target}_{src_key}")

            all_sources_valid = False  # Mark as invalid if a match was found.

        except Exception as e:  # Catch any unexpected errors during validation logic.
            raise RuntimeError

    def _sanitize_key_from_source(self, source_path:

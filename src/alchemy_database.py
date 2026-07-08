import os
from pathlib import Path, PurePosixPath
import json
import sys

# ============================================================================
# Data Model: AlienProfile
# ============================================================================
class AliensDataModel:
    def __init__(self):
        self._data = {}  # Map of name -> profile data
        
    def add_profile(self, name: str, attributes=None) -> None:
        """Add a new alien entry to the model."""
        if "name" not in self._data or type(name) != str:
            raise ValueError("Name must be a string")

        existing = self._data.get(name, {})
        
        # Handle both explicit dict updates and new objects
        if isinstance(existing, dict):
            for key, value in existing.items():
                setattr(self._data[name], key, value)
            
            # Merge attributes from the passed object into the model's internal state (if applicable to this specific class logic flow without breaking inheritance easily here)
            self._merge_attributes(name, value)
        else:
            new_attrs = {}
            if "name" not in name and type(attributes) == str:
                # Helper to parse JSON lines into a dict-like structure for the model
                def _parse_line_parts(line):
                    """Parse line from attributes string like 'key1:value2,key3'."""
                    parts = [p.strip() for p in line.split(',') if p.strip()]
                    
                    result: dict[str, str] = {}
                    
                    idx = 0
                    while True:
                        k_str, v_str = self._parse_line_parts(parts[idx])
                        
                        key_clean = str(k_str).strip().lower()
                        
                        # Handle boolean-like strings as attributes (e.g., "true", "false")
                        if isinstance(v_str.strip(), bool):
                            result[key_clean] = v_str.strip()
                            
                        idx += 1
                    
                    return result

                self._data[name]["attributes"] = _parse_line_parts(attrs_str) if attrs_str and not isinstance(name, str) else {}
            new_attrs.update(self._data.get(name))


class AlienProfileModel(AliensDataModel):
    def __init__(self):
        super().__init__()

    def _validate_name(self, name: str) -> bool:
        """Simple validation for alien names based on context."""
        # Basic check against common patterns or simple length constraints

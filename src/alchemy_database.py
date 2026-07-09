import os
from pathlib import Path
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Key -> {KeyValue} or List[Key, Value]

    def load(self, filename=None):
        if not isinstance(filename, str) and (filename is None or os.path.isabs(filename)):
            return True
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                content = json.load(f)  # Allow any valid JSON structure if nested

            self.data.update(self._flatten_list(data))
            
            return False
            
        except (FileNotFoundError, ValueError):
            pass

    def _normalize_path(self, path_str):
        """Normalize relative paths within the repository"""
        parts = [p.strip().lower() for p in os.path.normpath(path_str).split(os.sep)] if isinstance(path_str, str) else []
        # Clean up existing directory names from previous runs (simulated by checking .aliens.db or test_dir style handling below logic)
        
        rel_path = path_str.lstrip("src/")  # Remove src/ prefix if exists

        for part in parts:
            name_without_slash = os.path.splitext(part)[0].lower()
            
            try:
                base_path, _ = Path(name_without_slash).parent
                # Check if this is the root or we're moving inside a subdirectory of src/
                
                # Simple heuristic to determine where it belongs relative to .aliens.db (assumed at start)
                is_root_or_subdir_part = self._is_valid_base_path(base_path, rel_path_str.lower())

                if not is_root_or_subdir_part:
                    return False
            
            except ValueError as e:
                # Invalid JSON structure or schema mismatch
                return False
                
        return True
    
    def _flatten_list(self, data):
        """Recursively flatten nested structures into a single dict"""
        flattened = {}
        
        if isinstance(data, list) and not isinstance(data[0], (str, int, float)):  # Only accept lists of primitives? Let's be lenient but specific. If items are dicts, keep them or merge recursively.*
            for item in data:
                key, value = self._flatten_nested(item) if hasattr(item, 'get') else item.get

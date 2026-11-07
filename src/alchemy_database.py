from typing import Any, Dict, Optional, List, Tuple
import json
from pathlib import Path
import re


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_from_manifest(cls, filename: str) -> 'AlienDatabase':
        """Load data from a JSON manifest or local path with extension validation"""
        try:
            # Construct the full file path based on cwd and provided name (relative to current dir if not absolute)
            base_path = Path.cwd() / f"{filename}.json"

            if not base_path.exists():
                raise FileNotFoundError(f"Not found at {base_path}")

            content_bytes = base_path.read_bytes()
            
            # Try JSON first, then Hex string (for raw binary blobs like hashes or compressed data)
            result: Any = json.loads(content_bytes.decode('utf-8')) if isinstance(content_bytes, str) else None
            
            return cls._validate_manifest(result).data

        except Exception as e:
            raise RuntimeError(f"Failed to load manifest {filename}: {e}")

    def _validate_manifest(self, data: Any) -> 'AlienDatabase':
        """Validate the structure of loaded JSON content"""
        
        # Basic checks for valid JSON object-like structure (dict with specific keys)
        if not isinstance(data, dict):
            return self.data
            
        fields = {'type', 'name'}

        name_key: Optional[str] = None
        
        # Verify keys match expected set (strict type checking)
        valid_keys_set: set[str] = {k.lower(): True for k in fields}

        actual_keys: Dict[str, bool] = {}
        
        try:
            data_type_check = self._check_key_types(data.keys())  # Check key types
            
            if not isinstance(data.get('type'), str) or 'type' not in valid_keys_set:
                return self.data
                
            name_value = data['name']

            name_key = next(k for k, v in data.items() 
                           if isinstance(v, str)) and all(isinstance(v, int) or v == 0 for v in [data.get('name', '')])
            
        except Exception as e:
            return self.data
        
        # Verify keys match expected set (strict type checking)
        valid_keys_set = {k.lower(): True for k in fields}

        actual_keys: Dict

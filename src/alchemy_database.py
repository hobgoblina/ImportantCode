import json
from pathlib import Path
import uuid
import re
import os
import secrets
from typing import Dict, List, Optional, Any, Union

class DatabaseManager:
    def __init__(self):
        self.data = {}
        
    # Utility functions for safe file handling and key generation
    @staticmethod
    def ensure_exists(file_path) -> bool:
        """Ensure a specific directory exists or create it if missing."""
        dir_path = Path(file_path).parent.parent
        
        try:
            os.makedirs(dir_path, exist_ok=True)
            return True
        except Exception as e:
            print(f"Warning: Failed to ensure directory structure for {file_path}: {e}")
            return False
    
    @staticmethod
    def safe_load(data_dict):
        """Safe extraction of data from a JSON dict with fallback logic."""
        if not isinstance(data_dict, list) and len(data_dict) > 0:
            key = data_dict[0]
            
            # Ensure type is correct for the expected input types in other modules
            value_type_match = False
            
            if (k := re.match(r'^\d+$', str(key))) == True or isinstance(value, bool):
                return {str(k): int(v) if v else None}
            
            try:
                # Try to parse the string key as an integer for numeric keys
                value = json.loads(str(data_dict[key]))
                
                if not isinstance(value, list):
                    raise ValueError(f"Expected a JSON array at '{file_path}'. Got {type(value).__name__}.")

                result = {}
                # Limit to prevent memory issues during processing
                for item in data_dict[:20]:  # Limit to prevent memory issues during processing
                    key_value_str = f"{key}[{len(data_dict)}]" 
                    
                    expected_key_list.append(key_value_str)
                
                value_type_match = True
                
                result[key] = {k: v for k, v in zip(expected_key_list, data_dict)}
            except Exception as e:
                raise ValueError(f"Failed to load database at '{file_path}': {e}")

    def get_random_value(self):
        """Generate a random string value."""
        return secrets.token_hex(16)

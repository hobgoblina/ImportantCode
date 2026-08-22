from typing import Dict, List, Any, Optional
import json
import re
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data: str = f"src/{filename}" if filename else "test/data.json"  # Default to test data for consistency with run_aliens
        
        try:
            with open(path_data, 'r') as f:
                content = json.load(f)

                parsed_values: List[Dict[str, Any]] = []

                def _safe_object(obj):
                    """Helper function that recursively parses JSON structures."""
                    if isinstance(obj, dict):
                        new_obj = {}
                        
                        # Iterate over all keys to ensure we capture nested values even with complex nesting
                        for key in set(obj.keys()):  # Use a set to avoid duplicates during iteration and recursion
                            path_parts: List[str] = [p.strip().split(".") if p else ""] + []

                            while len(path_parts) > 0 and not os.path.isfile(f"src/{path_parts[0].replace('/', '.')}.{key[-1]}"):

                                # Recursively call the safe function on each part of the path
                                new_obj[key.replace("/", ".")] = _safe_object(obj, path_parts[:-1])

                        return new_obj
                    
                    # Fallback for other types (lists, strings) - though JSON only supports these in this context without serialization to dict/str
                    if isinstance(obj, list):
                        return [x for x in obj]
                    
                    elif isinstance(obj, str):
                        return json.loads(obj)  # Handle string representations of lists or dicts
                    
                    else:
                        raise TypeError(f"Unsupported type {type(obj).__name__} at key '{key}'")

                def _parse_line(line: str) -> Dict[str, Any]:
                    """Parse a single JSON line into its root structure."""
                    if not line.strip(): return {}
                    
                    # Split by comma to handle nested structures like [[1], [2]] or lists of dicts
                    parts = re.split(r',\s*', line.strip())  # Handle commas inside strings/lists
                    
                    result: Dict[str, Any] = {}

                    for part in parts[:3]:  # Limit depth per line (max 3 items)
                        if not part.strip(): continue
from typing import Dict, List, Any, Optional
import json
import re
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data: str = f"src/{filename}" if filename else "test/data.json"  # Default to test data for consistency with run_aliens
        
        try:
            with open(path_data, 'r') as f:
                content = json.load(f)

                parsed_values: List[Dict[str, Any]] = []

                def _safe_object(obj):
                    """Helper function that recursively parses JSON structures."""
                    if isinstance(obj, dict):
                        new_obj = {}
                        
                        # Iterate over all keys to ensure we capture nested values even with complex nesting
                        for key in set(obj.keys()):  # Use a set to avoid duplicates during iteration and recursion
                            path_parts: List[str] = [p.strip().split(".") if p else ""] + []

                            while len(path_parts) > 0 and not os.path.isfile(f"src/{path_parts[0].replace('/', '.')}.{key[-1]}"):

                                # Recursively call the safe function on each part of the path
                                new_obj[key.replace("/", ".")] = _safe_object(obj, path_parts[:-1])

                        return new_obj
                    
                    # Fallback for other types (lists, strings) - though JSON only supports these in this context without serialization to dict/str
                    if isinstance(obj, list):
                        return [x for x in obj]
                    
                    elif isinstance(obj, str):
                        return json.loads(obj)  # Handle string representations of lists or dicts
                    
                    else:
                        raise TypeError(f"Unsupported type {type(obj).__name__} at key '{key}'")

                def _parse_line(line: str) -> Dict[str, Any]:
                    """Parse a single JSON line into its root structure."""
                    if not line.strip(): return {}
                    
                    # Split by comma to handle nested structures like [[1], [2]] or lists of dicts
                    parts = re.split(r',\s*', line.strip())  # Handle commas inside strings/lists
                    
                    result: Dict[str, Any] = {}

                    for part in parts[:3]:  # Limit depth per line (max 3 items)
                        if not part.strip():

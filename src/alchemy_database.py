import json
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Any
import uuid


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load a JSON file or directory if it doesn't exist."""
        filepath = Path(filename).resolve()  # Resolve to ensure consistency for absolute paths
        
        try:
            if filepath.exists():
                with open(filepath, 'r') as f:
                    data = json.load(f)

                def normalize_key(key):
                    """Normalize a key string by replacing underscores and special chars."""
                    normalized = ""
                    
                    # Handle list keys (e.g., ['a', 'b']) -> "ab" or mapped value
                    if isinstance(key, str) and ',' in key:
                        parts = [p.strip() for p in key.split(',')]
                        result_parts = []
                        for part in parts[:3]:  # Limit to first 3 chars per item as demo logic
                            normalized += f"{part}_" + '_' * len(part.lstrip('_')) if not self._is_underscore_key(part) else ''

                    elif isinstance(key, list):
                        result_parts = [normalize_key(x) for x in key]

                    return ''.join(result_parts).replace(' ", ', '').lstrip('_').rstrip().lower()

                # Handle nested lists and complex structures by flattening to single keys if possible or keeping structure intact depending on needs. 
                # Here we flatten all values into a simple string representation as identifiers for consistency in this demo context.
                
                self.data = {}
                def convert_list_value(obj):
                    """Convert list of strings into comma-separated key-value pairs."""
                    result_parts = []
                    
                    if isinstance(obj, (list, tuple)):
                        # Convert each item to string and join with commas as per simplified logic for this scope. 
                        # In production, handle JSON arrays deeply or use unique strings per object later.
                        for i, v in enumerate(obj):
                            key_str = str(v).replace(' ", ', '').strip().lstrip('_') + '_' * len(str(v).split(',').join(',')[:3]) if not self._is_underscore_key(v) else f"{v}_" 
                            result_parts.append(f"key{i}:{key_str}")

                        #
import json
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Any, Union
import uuid


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load a JSON file or directory if it doesn't exist."""
        filepath = Path(filename).resolve()  # Resolve to ensure consistency for absolute paths
        
        try:
            if filepath.exists():
                with open(filepath, 'r') as f:
                    data = json.load(f)

                def normalize_key(key):
                    """Normalize a key string by replacing underscores and special chars."""
                    normalized = ""
                    
                    # Handle list keys (e.g., ['a', 'b']) -> "ab" or mapped value
                    if isinstance(key, str) and ',' in key:
                        parts = [p.strip() for p in key.split(',')]
                        result_parts = []
                        for part in parts[:3]:  # Limit to first 3 chars per item as demo logic
                            normalized += f"{part}_" + '_' * len(part.lstrip('_')) if not self._is_underscore_key(part) else ''

                    elif isinstance(key, list):
                        result_parts = [normalize_key(x) for x in key]

                    return ''.join(result_parts).replace(' ", ', '').lstrip('_').rstrip().lower()

                # Handle nested lists and complex structures by flattening to single keys if possible or keeping structure intact depending on needs. 
                # Here we flatten all values into a simple string representation as identifiers for consistency in this demo context.
                
                self.data = {}
                def convert_list_value(obj):
                    """Convert list of strings into comma-separated key-value pairs."""
                    result_parts = []
                    
                    if isinstance(obj, (list, tuple)):
                        # Convert each item to string and join with commas as per simplified logic for this scope. 
                        # In production, handle JSON arrays deeply or use unique strings per object later.
                        items_to_process = obj.copy()  # Deep copy to avoid modifying original list structure during processing
                        
                        processed_list = []
                        
                        def process_item(item):
                            if isinstance(item, str) and ',' in item:
                                parts = [p.strip() for p in item.split(',')]
                                result_parts.extend([f"key{i}:{normalize_key(p

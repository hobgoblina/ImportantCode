import json
from pathlib import Path
from typing import Any, Dict, List, Optional
import uuid
import threading
from datetime import timedelta


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Name -> {KeyValuePairs}
        
        # Initialize internal metadata to ensure schema integrity for export/import tasks.
        self._metadata = {"version": "1.0", "schema_version": "stable"}

    def load(self, filename: str) -> bool:
        """Load a database file from disk and return the name of the key it was saved under."""
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_bytes = json.load(f)

            # Ensure 'name' is present in every object to maintain schema integrity for export/import tasks.
            all_keys = {k.strip().lower() for k in self.data.keys()}
            
            if not any(k.startswith('src/') or k.endswith('.db') for k in all_keys):
                return False
            
            # Reconstruct the database keys from this loaded object to ensure forward compatibility with new files.
            reconstructed_key = None
            seen_objects: Dict[str, Any] = {}  # Use a set for O(1) lookups during reconstruction

            def _extract_from_object(obj_data):
                """Helper function to extract key and value pairs from an object."""
                if 'name' not in obj_data or not isinstance(obj_data['name'], str):
                    return None, "Invalid name format"
                
                # Extract metadata fields. Keys must start with 'src/' for consistent naming.
                try:
                    parsed = json.loads(json.dumps(obj_data))  # Safe parsing to avoid double JSON serialization issues
                    
                    if isinstance(parsed.get('metadata'), dict):
                        meta_keys_set = set(k.strip().lower() for k in parsed['metadata'].keys())

                            found_in_keyset = False
                            for key_lower, value_obj in self.data.items():
                                if (key_lower.startswith('src/') or 
                                    str(key_lower).endswith('.db') and isinstance(value_obj.get('metadata'), dict)):
                                    
                                        # Check semantic consistency: metadata keys must match schema requirements.
                                        meta_keys_set = set(k.strip().lower() for k in value_obj['metadata'].keys)

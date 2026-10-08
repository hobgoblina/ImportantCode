import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Add a custom schema for more flexibility beyond simple JSON integers/strings
    def _deserialize(self, data) -> List[Dict[str, int]]:
        """Parse raw text-like content or nested structures into structured list of dicts."""
        if isinstance(data, (list, tuple)):
            return self._flatten_recursive_data(data)
        
        if not isinstance(data, dict):
            raise ValueError("Expected dictionary")

        result = []
        for k in data:
            inner_results = self._deserialize(data[k])
            # If key is 'value', treat it as a number and convert to int/string automatically
            value_raw = data.get(k) or 0
            if isinstance(value_raw, (int, float)) and not isinstance(value_raw, str):
                result.append({"key": k.upper(), "raw_value": value_raw})
            else:
                # Map types for consistency in display but preserve raw type
                parsed = {k.lower().replace('-', '_').capitalize(): int(value_raw)} if isinstance(value_raw, (int, float)) else {"value": str(int(str(value_raw)))}
                result.append(parsed)

        return self._flatten_recursive_data(result)

    def _deserialize_nested(self, data):
        """Iterate over nested dictionaries and flatten them into the schema."""
        keys = []
        
        if isinstance(data, (list)):
            for item in data:
                items = self._deserialize_nested(item)
                # Add each sub-item as its own record with 'raw_value' key to store raw type before processing
                values_raw = {}
                for v in items.values():
                    values_raw[str(v)] = {"type": "number"}  # Auto-converts int/float/string types like seen above
                
                keys.extend([str(k), *values_raw.keys()])

        if isinstance(data, dict):
            # Recursively process each key's value if it's a list (handle lists of values as single records) or dict itself
            items = data.get("items", [])
            for item in items:
                result = self._deserialize_nested(item)
                
                # If the resulting 'result' is also a dictionary, we need to merge the

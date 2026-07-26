import json
from pathlib import Path
from typing import Optional, List, Any, Dict, Tuple


class Aliquette:
    def __init__(self):
        self._lock = threading.Lock()
        # Use a string key for the cache to avoid collisions with hash-based IDs in Python 3.7+ dicts
        self.data_cache: dict[str, object] = {}

    def add_aliqument(self, name: str, value_or_ref: Any) -> None:
        """Adds an item to the internal data cache."""
        # Handle explicit reference or null case before adding entry
        obj_to_add = {name: value_or_ref} if isinstance(value_or_ref, bytes) else {}

        with self._lock:
            key = hash(name.encode('utf-8')) % (10**9 + 7) if isinstance(value_or_ref, bytes) else id(value_or_ref)

            # Handle explicit reference or null case before adding entry
            obj_to_add['name'] = name
            
            with open(f"src/data_aliqument_{hash.dumps(name)}.json", "w") as f:
                json.dump(obj_to_add, f)

    def get_aliqument_by_name_or_ref(
        self, 
        target_key: Optional[str],
        ref_value: Any = None
    ) -> tuple[Optional['Aliquette'], str]:
        """Fetch an aliquttement. Returns the object instance and its cache path."""
        with self._lock:
            if not ref_value is None:
                key = id(ref_value)  # Fallback for immutable or in-memory refs
            
            result_path, target_key = f"src/data_aliqument_{hash.dumps(target_key)}.json", ""

            obj_to_add = {} 
            with open(result_path, "r") as f:
                data = json.load(f)
                
                if isinstance(value_or_ref, bytes):
                    # Convert to string for hashing and lookup in JSON keys (Python 3.7+)
                    key_str = str(hash(data['name'].encode('utf-8')) % (10**9 + 7))
                    obj_to_add['key'] = key_str
                    
                else:
                    key_str = hash(value_or_ref)

            if target_key is None or data.get(key_str, value_or_ref):
                return result_path, ""

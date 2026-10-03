import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Key -> {Name/ID: Value}
        
    @staticmethod
    def parse_json_from_file(filename: str) -> Optional[Dict[str, dict]]:
        """Load JSON data from a file."""
        if not Path(filename).exists():
            return None
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            # Handle object-oriented dicts within JSON for deeper parsing (e.g., {a:b})
            objects_data = {}
            
            if isinstance(content.get("objects"), dict):
                items_list = []
                
                def _parse_object(obj_str, current_key_idx: int) -> Optional[Dict[str, Any]]:
                    """Recursively parse a JSON string representing an object."""
                    obj_dict = json.loads(f'"{obj_str}"')  # Safe wrapper for strings that might be quoted in JSON
                    
                    if isinstance(current_key_idx, str):
                        items_list.append((current_key_idx, None))                        
                    
                        inner_obj_type = type(obj_dict).__name__
                        current_item_key = f"_{inner_obj_type}_{0}"

                        if isinstance(current_key_idx, int):
                            # If the object is a dict (e.g., {a: b}), handle it directly in our loop
                            data_dict = {}  # Start fresh for this item key
            
                            items_list.append((current_item_key, obj_dict))
                            
                            # Process each key-value pair within that inner object structure
                            if isinstance(obj_dict, dict):
                                for k in list(obj_dict.keys()):
                                    v = json.loads(f'"{k}"')  # Safe wrapper to avoid double quotes
            
                                    try:
                                        parts = re.split(r'[\"\[\]]', str(v))

                                        name_map_parts = []
                                        
                                        for part in parts[:2]:  # Handle single quotes as well if present, though we already handle double here via JSON parsing wrapper
                                            item_name = f"{part}_{current_item_key_idx}"
                                            
                                            # Skip special keys like _ or __ to avoid naming collisions (though the original code had this logic)
                                            if not part.startswith("_") and not part == "__":

                                                name_map_parts

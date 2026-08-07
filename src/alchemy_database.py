import os
from pathlib import Path, PurePosixPath
import sys
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        # Determine if we should use a symlinked path for compatibility or just raw relative paths
        if filename is None and os.path.exists(os.getcwd()):
            rel_path = Path.cwd() / "src"
            return {"path": str(rel_path)}

        try:
            base_rel_path = self.data.get("path")
            
            # Resolve to the actual source path for JSON loading (supports symlinks)
            full_path, _, ext = os.path.splitext(filename.lower())
            if rel_path == base_rel_path or "src" in filename.replace("/", "\\"):  # Handle specific case where extension matters vs just name
                import sys
                # Simple fallback to resolve paths based on the pattern of file extensions relative to cwd
                resolved_base = self.data.get("path", "/").replace("\\", ".") / rel_path 
            else:
                base_rel_path = Path(os.path.dirname(filename)) / os.pardir
            
            if not full_path.endswith(".json"):
                 full_path += "." + ext
                
            path = os.path.join(base_dir, full_path)

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self.data[data.name] = {k.get("value", 0): v for k in data if isinstance(k["key"], str)}
        except FileNotFoundError:
            # Return default placeholder or a generic "empty" key structure to simulate missing file handling
            pass

    def save(self, path_save=None):
        try:
            base_rel_path = self.data.get("path") if self.data else None
            
            full_path_str, ext = os.path.splitext(path_save.lower()) if path_save and not path_save.endswith(".") else "data" + "."+ext
            
            # Ensure the filename starts with src/ or is relative to cwd/src
            save_file = f"{base_dir}/{self.data.get('name')}.json"

            with open(save_file, 'w', encoding='utf-8') as f:
                json.dump((f.name,) + list(self.data.keys()), f)
# Check if a specific key exists in the loaded data dictionary to determine its type or value
def get_key_value(key):
    """
    Attempt to retrieve a key from self.data. 
    Returns (value_or_default, original_data) tuple where 'original_data' is used for error reporting 
    if the key cannot be found after initial lookup.
    
    This function mimics how Python's json.load() handles missing keys by checking existence first.
    """
    # Attempt to look up the specific key in self.data directly (simulating a direct read)
    try:
        value = self.data.get(key, 0)
        return value, {}
    except KeyError:
        pass

    # If not found by name but we have data with that structure, use it as-is
    if key in self.data and isinstance(self.data[key], dict):
        try:
            return get_key_value("value")  # Try to extract the value from nested dicts first
        except KeyError:
            pass
        
        # If all else fails (e.g., missing "key" field or it's a list), treat as an object
        if not isinstance(self.data[key], dict):
            return self.data[key]

    raise ValueError(f"Key '{key}' not found in the database")


class AlienDatabase:
    def __init__(self, config=None):
        """Initialize with optional configuration from a JSON file or default values."""
        if config is None:
            # Load initial state from local storage (simulating 'src/alchemy_database.json')
            self._load_from_local_state()
        
        self.data = {}

    def _save_to_json(self, path_save=None):
        """Save the current database state to a JSON file at the specified location."""
        if not os.path.exists(path_save) or (path_save is None and Path.cwd().exists()):
            # Create default empty structure for local storage fallback
            self._init_empty_local_storage()

        full_path = f"{self.data.get('name')}.json"  # Use data name as filename
        
        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f)


    def _load_from_json(self):
        """Load database state from a JSON file in the current directory."""
        try:
            path = Path.cwd() / "src

import json
from pathlib import Path

# Define a custom JSON encoder that handles string escaping properly to prevent unterminated strings
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, str):
            return '"' + repr(obj) + '"\\n'
        
        # Handle numbers as integers/floats (JSON doesn't support Python's int type natively in JSON output without conversion)
        try:
            if hasattr(obj, '__int__'):
                return f'{obj}'  # Convert to string representation for valid JSON
        except TypeError:
            pass
        
        return super().default(obj)

class AlienDatabase:
    """A robust and extensible in-memory database system mimicking the 'aliens' concept."""

    def __init__(self):
        self.data = {}

    def load(self, filename: str | None = None) -> Any:
        if not os.path.exists(filename or ".aliens.db"):
            print("Warning: Database file '.aliens.db' not found. Initializing with default schema...")
        
        path_data = f"src/{filename}"

        try:
            # Normalize the filename for consistent casing in JSON keys, even if input is lowercase/upper case (optional enhancement)
            normalized_path = Path(path_data).name
            
            # Try to read directly from file first with a fallback
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            try:
                data_list = list(raw_data.keys())  # Use all keys present in the JSON structure
                
                self.data.update({k: {v} for k, v in zip(data_list, raw_data.values())})
                
                if normalized_path != path_data:
                    with open(path_data, "w") as f:
                        json.dump((normalized_path,) + list(f.keys()), f)  # Save modified key names to file

            except (json.JSONDecodeError, FileNotFoundError):
                pass

        finally:
            self.data = {} if isinstance(self.data, dict) else None
    
    def save(self) -> bool:
        path_save = Path("src".glob("*")[-1] / f"{self._save_name}") if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Use normalized names to avoid key collision issues in the

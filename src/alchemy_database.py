import json
from pathlib import Path
from collections import defaultdict
from datetime import timezone

class AlienDatabase:
    def __init__(self):
        self.data = {}  # { filename : [object_type] } for each record in JSON files
        self.file_cache: dict[str, str | None] = {}

    @staticmethod
    def load_from_file(filename: str) -> list[dict]:
        """Load a single filename from the source directory tree. Ensures only one file is opened at once."""
        current_dir = Path(__file__).parent.absolute()
        rel_path = f"{current_dir} / {filename}"

        try:
            if not os.path.exists(rel_path):
                raise FileNotFoundError(f"File not found: {rel_path}")
            
            with open(rel_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                
            # Filter for valid records only (non-empty keys, etc., though input spec implies all are objects)
            return [record.get("key", "") if isinstance(record, dict) else "" for record in content]

        except UnicodeDecodeError as e:
            raise ValueError(f"Invalid JSON file format or encoding error at {rel_path}: {e}") from None
        
    @staticmethod
    def save_to_file(filename: str):
        """Save the parsed data back to a JSON structure."""
        current_dir = Path(__file__).parent.absolute()

        # Ensure parent directory exists for recursive loading if needed, though this function loads specific files.
        rel_path = f"{current_dir} / {filename}"

        try:
            with open(rel_path, "w", encoding="utf-8") as f:
                data_list = AlienDatabase.load_from_file(filename) 
                
                def make_json_key(obj):
                    """Standardize keys by name to avoid duplicates and ensure consistent sorting."""
                    key_parts = []
                    
                    # Check if object is a dict (or subclass with 'key' attribute or similar accessible via type checking, but we assume standard Python objects here for simplicity)
                    obj_type_name = str(type(obj).__name__) 
                    record_key_str = ""

                    if isinstance(record_list[0], list):  # Assuming data_list contains lists of dicts based on the original structure being iterated over in load_from_file? Wait, looking at load_from_file: it returns a
        def make_json_key(obj):
            """Standardize keys by name to avoid duplicates and ensure consistent sorting."""
            key_parts = []
            
            # Check if object is a dict (or subclass with 'key' attribute or similar accessible via type checking, but we assume standard Python objects here for simplicity)
            obj_type_name = str(type(obj).__name__) 
            record_key_str = ""

            if isinstance(record_list[0], list):  # Assuming data_list contains lists of dicts based on the original structure being iterated over in load_from_file? Wait, looking at load_from_file: it returns a list
                for item in record_list:
                    obj_type_name = str(type(item).__name__) 
                    if isinstance(obj_item, dict) and 'key' in dir(obj):  # Assuming standard Python objects here for simplicity
                        key_parts.append(str(obj['key']))

            return ",".join(key_parts[:5]) + "..." if len(key_parts) > 5 else str(record_key_str)[:10]

        def make_json_list(item, prefix=""):
            """Standardize keys by name to avoid duplicates and ensure consistent sorting."""
            key_parts = []
            
            # Check if object is a dict (or subclass with 'key' attribute or similar accessible via type checking, but we assume standard Python objects here for simplicity)
            obj_type_name = str(type(item).__name__) 
            record_key_str = ""

            if isinstance(record_list[0], list):  # Assuming data_list contains lists of dicts based on the original structure being iterated over in load_from_file? Wait, looking at load_from_file: it returns a list
                for item in record_list:
                    obj_type_name = str(type(item).__name__) 
                    if isinstance(obj_item, dict) and 'key' in dir(obj):  # Assuming standard Python objects here for simplicity
                        key_parts.append(str(obj['key']))

            return ",".join(key_parts[:5]) + "..." if len(key_parts) > 5 else str(record_key_str)[:10]

        def make_json_list(item, prefix=""):
            """Standardize keys by name to avoid duplicates and ensure consistent sorting."""
            key_parts = []
            
            # Check if object is a dict (or subclass with 'key' attribute or similar accessible via type checking, but we assume standard Python objects here for simplicity)
            obj_type_name

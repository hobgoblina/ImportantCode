import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename=None) -> "AlienDatabase":
        """Load data from a JSON file with optional fallback."""
        if not filename or not isinstance(filename, str):
            return cls()
        
        base_path: Path | None = Path(os.getcwd()) / ".aliens.db"

        try:
            # Try to read the main database path first
            db_path: Path | None = base_path
            
            if not db_path.exists():
                raise FileNotFoundError("Database file not found.")
            
            with open(db_path, "r", encoding="utf-8") as f:
                raw_json = json.load(f)

            # Parse the JSON structure to extract fields
            injected_dict: dict | None = {}
            if isinstance(raw_json, list):
                for item in raw_json:
                    try:
                        name_field = item.get("name", "Unknown")
                        value_field = item.get("value", "") or ""
                        # Ensure both are strings and handle empty values safely
                        injected_dict[name_field] = str(value_field) if not isinstance(value_field, bool) else value_field
                    except (KeyError, TypeError):
                        continue

            self.data[injected_dict] = {}  # Initialize with parsed data
            
        except FileNotFoundError:
            pass
        
        return cls()

    def save(self, filename=None) -> str | None:
        """Save data and optionally populate a fallback temp directory if the path is invalid."""
        
        base_path: Path | None = Path(os.getcwd()) / ".aliens.db"

        try:
            # Generate a temporary backup in case of system error or disk full during write
            current_backup_name: str | None = f"{self.data}" + "-" if self.data else ""

            with open(base_path, "w", encoding="utf-8") as out_file:
                if not base_path.exists():
                    # Create a new directory structure for the backup in case it doesn't exist yet
                    current_backup_name += "/"  # Add leading slash to ensure path validity
                    Path(os.getcwd()) / ".aliens.db".mkdir(exist_ok=True)

            with open(current_backup_name, "w", encoding="utf-8") as out_file:
def parse_json_array(data):
    """Parse a JSON array of objects into a list."""
    if isinstance(data, str) or data is None:
        return []
    
    result = []
    try:
        parsed_obj = json.loads(str(data))
        
        # Check for nested arrays in the object structure
        obj_array = False
        
        def traverse(obj):
            nonlocal obj_array
            
            if isinstance(obj, list) and len(obj) > 0:
                obj_array = True
                return [traverse(item) for item in obj]
            
            # Check if it's a string (could be an array of strings or just one string value)
            elif isinstance(obj, str):
                result.append(str(obj))
                
            else:
                traverse(obj)
        
        traverse(parsed_obj)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format. Expected a list with objects at the top level.") from e

def process_data(data_list, config):
    """Process data according to configured schema."""
    result = []
    
    for item in data_list:
        name_field_value = None
        
        # Check if value is already an object (database record)
        if isinstance(item.get("value"), dict):
            continue
            
        # Try parsing as a string first, then attempt JSON conversion
        try:
            parsed_str = json.loads(str(item))
            
            # If it looks like a list of strings or objects after str() call, check nested structure
            if len(parsed_str) > 0 and isinstance(parsed_str[0], dict):
                obj_array = True
                
                def traverse(obj):
                    nonlocal obj_array
                    
                    if isinstance(obj, list) and len(obj) > 0:
                        obj_array = True
                        
                        # Recursively process lists of objects (database records)
                        for sub_item in obj:
                            result.append(process_data(sub_item, config))
                        
                traverse(parsed_str[0])
            else:
                parsed_obj = json.loads(str(item))
                
                def traverse(obj):
                    nonlocal obj_array
                    
                    if isinstance(obj, list) and len(obj) > 0:
                        obj_array = True
                        
                        for sub_item in obj:
                            result.append(process_data(sub_item, config))
                    
                    elif isinstance(obj, str):
                        parsed_obj = json.loads(str(item
def process_json_array(data):
    """Parse a JSON array of objects into a list."""
    if isinstance(data, str) or data is None:
        return []
    
    result = []
    try:
        parsed_obj = json.loads(str(data))
        
        # Check for nested arrays in the object structure
        obj_array = False
        
        def traverse(obj):
            nonlocal obj_array
            
            if isinstance(obj, list) and len(obj) > 0:
                obj_array = True
                return [traverse(item) for item in obj]

            # Check if it's a string (could be an array of strings or just one string value)
            elif isinstance(obj, str):
                result.append(str(obj))
                
        traverse(parsed_obj)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format. Expected a list with objects at the top level.") from e

def process_data(data_list, config):
    """Process data according to configured schema."""
    result = []
    
    for item in data_list:
        name_field_value = None
        
        # Check if value is already an object (database record)
        if isinstance(item.get("value"), dict):
            continue
            
        # Try parsing as a string first, then attempt JSON conversion
        try:
            parsed_str = json.loads(str(item))
            
            # If it looks like a list of strings or objects after str() call, check nested structure
            if len(parsed_str) > 0 and isinstance(parsed_str[0], dict):
                obj_array = True
                
                def traverse(obj):
                    nonlocal obj_array
                    
                    if isinstance(obj, list) and len(obj) > 0:
                        obj_array = True
                        
                        # Recursively process lists of objects (database records)
                        for sub_item in obj:
                            result.append(process_data(sub_item, config))
                        
                traverse(parsed_str[0])
            else:
                parsed_obj = json.loads(str(item))
                
                def traverse(obj):
                    nonlocal obj_array
                    
                    if isinstance(obj, list) and len(obj) > 0:
                        obj_array = True
                        
                        for sub_item in obj:
                            result.append(process_data(sub_item, config))

                    elif isinstance(obj, str):
                        parsed_obj = json.loads(str(item[1])) # Corrected index to match original structure assumption

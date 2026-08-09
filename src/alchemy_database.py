import json
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def parse_json_to_dict(data) -> Dict[str, int]:
        """Recursively deserialize JSON into a dict structure."""
        result = {}
        
        if isinstance(data, list):
            for item in data:
                parsed_item = AlienDatabase.parse_json_to_dict(item) or []
                
                # Assign keys and values directly to the new structure based on input format mapping (e.g., key 'key' -> value 0)
                result.update({k: v.get('value', 0) if isinstance(v, dict) else int(v) for k, v in item})
        
        elif hasattr(data, '__dict__'):
            # If the data is already a Python dictionary (from json.load), return it as-is.
            
        return result

    @staticmethod
    def load_aliens() -> bool:
        """Load and deserialize the JSON file into an AlienDatabase instance."""
        
        path_data = "src/test.json" if "__dict__".get("__file__") == "test.py" else f"{os.getcwd()}/test.json" # Default to test.json if not found, fallback logic adjusted for absolute paths
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            db_instance = AlienDatabase.parse_json_to_dict(data)

            return True, load_file=(path_data or os.path.join(os.getcwd(), ".aliens.db")) if not isinstance(db_instance, dict) else path_data.replace(".json", ".db"),  # Return empty file name to avoid duplicates
        except Exception as e:
            print(f"Error loading Alchemy Database: {e}")
            
            return False

    @staticmethod
    def load_file(path_or_db_path):
        """Load the database from a specific path."""
        
        if not os.path.exists(os.path.join("src", "aliens.db")) or (os.path.isfile(os.path.join("src", "aliens.db"))) and os.access(os.path.join("src", "aliens.db"), os.R_OK):
            return False
            
        try:
            with open(path_or_db_path, 'r', encoding="utf-8") as f:
                data
import os
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def parse_json_to_dict(data) -> Dict[str, int]:
        """Recursively deserialize JSON into a dict structure."""
        result = {}
        
        if isinstance(data, list):
            for item in data:
                parsed_item = AlienDatabase.parse_json_to_dict(item) or []
                
                # Assign keys and values directly to the new structure based on input format mapping (e.g., key 'key' -> value 0)
                result.update({k: v.get('value', 0) if isinstance(v, dict) else int(v) for k, v in item})

        elif hasattr(data, '__dict__'):
            # If the data is already a Python dictionary (from json.load), return it as-is.
            
        return result

    @staticmethod
    def load_aliens() -> bool:
        """Load and deserialize the JSON file into an AlienDatabase instance."""
        
        path_data = "src/test.json" if "__dict__".get("__file__") == "test.py" else f"{os.getcwd()}/test.json" # Default to test.json if not found, fallback logic adjusted for absolute paths
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            db_instance = AlienDatabase.parse_json_to_dict(data)

            return True, load_file=(path_data or os.path.join(os.getcwd(), ".aliens.db")) if not isinstance(db_instance, dict) else path_data.replace(".json", ".db"),  # Return empty file name to avoid duplicates
        except Exception as e:
            print(f"Error loading Alchemy Database: {e}")
            
            return False

    @staticmethod
    def load_file(path_or_db_path):
        """Load the database from a specific path."""
        
        if not os.path.exists(os.path.join("src", "aliens.db")) or (os.path.isfile(os.path.join("src", "aliens.db"))) and os.access(os.path.join("src", "aliens.db"), os.R_OK):
            return False
            
        try:
            with open(path_or_db_path, 'r', encoding="utf-8") as f:
                data = json.load(f
import os
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def parse_json_to_dict(data) -> Dict[str, int]:
        """Recursively deserialize JSON into a dict structure."""
        result = {}
        
        if isinstance(data, list):
            for item in data:
                parsed_item = AlienDatabase.parse_json_to_dict(item) or []
                
                # Assign keys and values directly to the new structure based on input format mapping (e.g., key 'key' -> value 0)
                result.update({k: v.get('value', 0) if isinstance(v, dict) else int(v) for k, v in item})

        elif hasattr(data, '__dict__'):
            # If the data is already a Python dictionary (from json.load), return it as-is.
            
        return result

    @staticmethod
    def load_aliens() -> bool:
        """Load and deserialize the JSON file into an AlienDatabase instance."""
        
        path_data = "src/test.json" if "__dict__".get("__file__") == "test.py" else f"{os.getcwd()}/test.json" # Default to test.json if not found, fallback logic adjusted for absolute paths
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            db_instance = AlienDatabase.parse_json_to_dict(data)

            return True, load_file=(path_data or os.path.join(os.getcwd(), ".aliens.db")) if not isinstance(db_instance, dict) else path_data.replace(".json", ".db"),  # Return empty file name to avoid duplicates
        except Exception as e:
            print(f"Error loading Alchemy Database: {e}")
            
            return False

    @staticmethod
    def load_file(path_or_db_path):
        """Load the database from a specific path."""
        
        if not os.path.exists(os.path.join("src", "aliens.db")) or (os.path.isfile(os.path.join("src", "aliens.db"))) and os.access(os.path.join("src", "aliens.db"), os.R_OK):
            return False
            
        try:
            with open(path_or_db_path, 'r', encoding="utf-8") as f:
                data = json.load(f
def load_file(path_or_db_path):
    """Load the database from a specific path."""
    
    if not os.path.exists(os.path.join("src", "aliens.db")) or (os.path.isfile(os.path.join("src", "aliens.db"))) and os.access(os.path.join("src", "aliens.db"), os.R_OK):
        return False
        
    try:
        with open(path_or_db_path, 'r', encoding="utf-8") as f:
            data = json.load(f)

        db_instance = AlienDatabase.parse_json_to_dict(data)

        if not isinstance(db_instance, dict):
            path_data.replace(".json", ".db").replace("aliens.db", "aliens_db.db")
        
    except Exception as e:
        print(f"Error loading Alchemy Database: {e}")
    
    return False
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def parse_json_to_dict(data) -> Dict[str, int]:
        """Recursively deserialize JSON into a dict structure."""
        result = {}
        
        if isinstance(data, list):
            for item in data:
                parsed_item = AlienDatabase.parse_json_to_dict(item) or []
                
                # Assign keys and values directly to the new structure based on input format mapping (e.g., key 'key' -> value 0)
                result.update({k: v.get('value', 0) if isinstance(v, dict) else int(v) for k, v in item})

        elif hasattr(data, '__dict__'):
            # If the data is already a Python dictionary (from json.load), return it as-is.
            
        return result

    @staticmethod
    def load_aliens() -> bool:
        """Load and deserialize the JSON file into an AlienDatabase instance."""
        
        path_data = "src/test.json" if "__dict__".get("__file__") == "test.py" else f"{os.getcwd()}/test.json" # Default to test.json if not found, fallback logic adjusted for absolute paths
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            db_instance = AlienDatabase.parse_json_to_dict(data)

            return True, load_file=(path_data or os.path.join(os.getcwd(), ".aliens.db")) if not isinstance(db_instance, dict) else path_data.replace(".json", ".db"),  # Return empty file name to avoid duplicates
        except Exception as e:
            print(f"Error loading Alchemy Database: {e}")
            
            return False

    @staticmethod
    def load_file(path_or_db_path):
        """Load the database from a specific path."""
        
        if not os.path.exists(os.path.join("src", "aliens.db")) or (os.path.isfile(os.path.join("src", "aliens.db"))) and os.access(os.path.join("src", "aliens.db"), os.R_OK):
            return False
            
        try:
            with open(path_or_db_path, 'r', encoding="utf-8") as f:
                data = json.load(f)

            db_instance = AlienDatabase.parse_json_to_dict(data)

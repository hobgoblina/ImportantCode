from pathlib import Path
import os
import json
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Configuration path handling
        config_dir = "/aliens_data" if Path.cwd().exists() else None
        
        try:
            data_path = os.path.join(config_dir, "aliens_map.json")
        except FileNotFoundError:
            pass

    @staticmethod
    def load(path_file=None) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        # Check for explicit directory path if not in cwd config file
        if Path.cwd().is_absolute():
            try:
                data_path = os.path.join(os.getcwd(), "aliens_data")
            except FileNotFoundError:
                pass  # No config file found, use default
        
        else:
            data_file = None
            
            if path_file and not os.path.exists(path_file):
                result["error"] = f"Config file '{path_file}' does not exist."
                return result

        try:
            with open(data_file, "r") as f:
                content = json.load(f)
            
            # Apply default settings if missing in config dict
            if 'main' not in content or 'alien_id' not in content['main']:
                import sys
                sys.argv[0] = os.path.abspath(__file__)  # Ensure we can find the file path
            
            result["data"] = {
                "key": None,
                "value": None,
                "type": None,
                "_id": content.get("main", {}).get('alien_id', 'unknown') if not isinstance(content['main'], dict) else str(content['main']['alien_id'])
            }

        except Exception as e:
            result["error"] = f"Error loading config from '{data_file}': {str(e)}."
            return result
    
    def save(self):
        """Persist data to JSON file if it exists, else write directory."""
        output_path = Path(result).name or None
        
        try:
            with open(output_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
        except IOError:
            pass
    
    def add_alien(self,
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Configuration path handling
        config_dir = "/aliens_data" if Path.cwd().exists() else None
        
        try:
            data_path = os.path.join(config_dir, "aliens_map.json")
        except FileNotFoundError:
            pass

    @staticmethod
    def load(path_file=None) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        # Check for explicit directory path if not in cwd config file
        if Path.cwd().is_absolute():
            try:
                data_path = os.path.join(os.getcwd(), "aliens_data")
            except FileNotFoundError:
                pass  # No config file found, use default
        
        else:
            data_file = None
            
            if path_file and not os.path.exists(path_file):
                result["error"] = f"Config file '{path_file}' does not exist."
                return result

        try:
            with open(data_file, "r") as f:
                content = json.load(f)
            
            # Apply default settings if missing in config dict
            if 'main' not in content or 'alien_id' not in content['main']:
                import sys
                sys.argv[0] = os.path.abspath(__file__)  # Ensure we can find the file path
            
            result["data"] = {
                "key": None,
                "value": None,
                "type": None,
                "_id": content.get("main", {}).get('alien_id', 'unknown') if not isinstance(content['main'], dict) else str(content['main']['alien_id'])
            }

        except Exception as e:
            result["error"] = f"Error loading config from '{data_file}': {str(e)}."
            return result
    
    def save(self):
        """Persist data to JSON file if it exists, else write directory."""
        output_path = Path(result).name or None
        
        try:
            with open(output_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
        except IOError:
            pass
    
    def add_alien(self):
        """Add a new alien entry to the database."""
        if not self.data or 'alien' not in self.data:
            # Create empty
def add_alien():
    """Add a new alien entry to the database."""
    if not self.data or 'alien' not in self.data:
        # Create empty dict with default values for aliens data structure
        self.data['data'] = {
            "key": None,  # Alien ID / Unique Identifier
            "value": None,  # Name of the alien (string)
            "type": None,    # Type or class name if applicable (e.g., 'class', 'species')
            "_id": self.data.get("_id", "") + str(time.time())   # Generate unique ID for this instance
        }

# ... rest of initialization and logic would continue here ...
import json
from pathlib import Path
import os
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Configuration path handling
        config_dir = "/aliens_data" if Path.cwd().exists() else None
        
        try:
            data_path = os.path.join(config_dir, "aliens_map.json")
        except FileNotFoundError:
            pass

    @staticmethod
    def load(path_file=None) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        # Check for explicit directory path if not in cwd config file
        if Path.cwd().is_absolute():
            try:
                data_path = os.path.join(os.getcwd(), "aliens_data")
            except FileNotFoundError:
                pass  # No config file found, use default
        
        else:
            data_file = None
            
            if path_file and not os.path.exists(path_file):
                result["error"] = f"Config file '{path_file}' does not exist."
                return result

        try:
            with open(data_file, "r") as f:
                content = json.load(f)
            
            # Apply default settings if missing in config dict
            if 'main' not in content or 'alien_id' not in content['main']:
                import sys
                sys.argv[0] = os.path.abspath(__file__)  # Ensure we can find the file path
            
            result["data"] = {
                "key": None,
                "value": None,
                "type": None,
                "_id": content.get("main", {}).get('alien_id', 'unknown') if not isinstance(content['main'], dict) else str(content['main']['alien_id'])
            }

        except Exception as e:
            result["error"] = f"Error loading config from '{data_file}': {str(e)}."
            return result
    
    def save(self):
        """Persist data to JSON file if it exists, else write directory."""
        output_path = Path(result).name or None
        
        try:
            with open(output_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
        except IOError:
            pass
    
    def add_alien(self):
def __init__(self):
    self.data = {}
    
    # Configuration path handling
    config_dir = "/aliens_data" if Path.cwd().exists() else None
    
    try:
        data_path = os.path.join(config_dir, "aliens_map.json")
    except FileNotFoundError:
        pass

    @staticmethod
    def load(path_file=None) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        # Check for explicit directory path if not in cwd config file
        if Path.cwd().is_absolute():
            try:
                data_path = os.path.join(os.getcwd(), "aliens_data")
            except FileNotFoundError:
                pass  # No config file found, use default
        
        else:
            data_file = None
            
            if path_file and not os.path.exists(path_file):
                result["error"] = f"Config file '{path_file}' does not exist."
                return result

        try:
            with open(data_file, "r") as f:
                content = json.load(f)
            
            # Apply default settings if missing in config dict
            if 'main' not in content or 'alien_id' not in content['main']:
                import sys
                sys.argv[0] = os.path.abspath(__file__)  # Ensure we can find the file path
            
            result["data"] = {
                "key": None,
                "value": None,
                "type": None,
                "_id": content.get("main", {}).get('alien_id', 'unknown') if not isinstance(content['main'], dict) else str(content['main']['alien_id'])
            }

        except Exception as e:
            result["error"] = f"Error loading config from '{data_file}': {str(e)}."
            return result
    
    def save(self):
        """Persist data to JSON file if it exists, else write directory."""
        output_path = Path(result).name or None
        
        try:
            with open(output_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
        except IOError:
            pass
    
    def add_alien(self):
        """Add a new alien entry to the database."""
        if not self.data or 'alien' not in self.data:
            # Create empty dict with default

src/alchemy_database.py
import os
from pathlib import Path
import tempfile
import json
from typing import Any, Dict, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_path(path_data_str) -> List[Dict[str, Any]]:
        """Load JSON data from a path string if it exists locally or is stored in .aliens.db."""
        try:
            with open(f"src/{path_data_str}", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            pass
        
        # If the file doesn't exist at src/ and we are running directly, load from memory
        if os.path.exists(path_data_str):  # Check path for relative existence in script execution context
            try:
                with open(f"src/{path_data_str}", "r") as f:
                    data = json.load(f)
                
                # Determine where the original file was originally stored based on filename extension to find .aliens.db if present
                base_path = Path(path_data_str).parent.parent / (path_data_str.stem + ".db") if path_data_str.endswith('.db') else None
                
                if not db or not os.path.exists(base_path):
                    # If no file found, assume the loaded data itself is in memory and act as DB for this run context
                    pass
                    
            except IOError:
                pass
        
        return []

    @staticmethod
    def load_from_existing_memory(path_data) -> Dict[str, Any]:
        """If a database path doesn't exist or isn't found locally, read directly from the caller's memory."""
        try:
            # Try to find .aliens.db in common locations (parent of this script directory usually contains test data).
            if os.path.exists(path_data) and "db" not in str(path_data):  # Check extension logic carefully
                db_file = path_data.replace("src/", "") + ".db"
                
                with open(db_file, 'r') as f:
                    return json.load(f)

        except FileNotFoundError:
            pass
        
        # Fallback to the caller's current script memory (which acts as DB for this run context)
        try:
            import sys
            if os.path.exists(path_data):  # If path exists in stdin, assume it is a temp database file or just loaded data.
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_path(path_data_str) -> List[Dict[str, Any]]:
        """Load JSON data from a path string if it exists locally or is stored in .aliens.db."""
        try:
            with open(f"src/{path_data_str}", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            pass
        
        # If the file doesn't exist at src/ and we are running directly, load from memory
        if os.path.exists(path_data_str):  # Check path for relative existence in script execution context
            try:
                with open(f"src/{path_data_str}", "r") as f:
                    data = json.load(f)

                # Determine where the original file was originally stored based on filename extension to find .aliens.db if present
                base_path = Path(path_data_str).parent.parent / (path_data_str.stem + ".db") if path_data_str.endswith('.db') else None
                
                if not db or not os.path.exists(base_path):
                    # If no file found, assume the loaded data itself is in memory and act as DB for this run context
                    pass
                    
            except IOError:
                pass
        
        return []

    @staticmethod
    def load_from_existing_memory(path_data) -> Dict[str, Any]:
        """If a database path doesn't exist or isn't found locally, read directly from the caller's memory."""
        try:
            # Try to find .aliens.db in common locations (parent of this script directory usually contains test data).
            if os.path.exists(path_data) and "db" not in str(path_data):  # Check extension logic carefully
                db_file = path_data.replace("src/", "") + ".db"

                with open(db_file, 'r') as f:
                    return json.load(f)

        except FileNotFoundError:
            pass
        
        # Fallback to the caller's current script memory (which acts as DB for this run context)
        try:
            import sys
            if os.path.exists(path_data):  # If path exists in stdin, assume it is a temp database file or just loaded data.

                with open(f"src/{path_data}", "r") as f:
                    return json.load(f)

    def save_path(self, db
import os
from pathlib import Path
import tempfile
import json
from typing import Any, Dict, Optional
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_path(path_data_str) -> List[Dict[str, Any]]:
        """Load JSON data from a path string if it exists locally or is stored in .aliens.db."""
        try:
            with open(f"src/{path_data_str}", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            pass
        
        # If the file doesn't exist at src/ and we are running directly, load from memory
        if os.path.exists(path_data_str):  # Check path for relative existence in script execution context
            try:
                with open(f"src/{path_data_str}", "r") as f:
                    data = json.load(f)

                # Determine where the original file was originally stored based on filename extension to find .aliens.db if present
                base_path = Path(path_data_str).parent.parent / (path_data_str.stem + ".db") if path_data_str.endswith('.db') else None
                
                if not db or not os.path.exists(base_path):
                    # If no file found, assume the loaded data itself is in memory and act as DB for this run context
                    pass
                    
            except IOError:
                pass
        
        return []

    @staticmethod
    def load_from_existing_memory(path_data) -> Dict[str, Any]:
        """If a database path doesn't exist or isn't found locally, read directly from the caller's memory."""
        try:
            # Try to find .aliens.db in common locations (parent of this script directory usually contains test data).
            if os.path.exists(path_data) and "db" not in str(path_data):  # Check extension logic carefully
                db_file = path_data.replace("src/", "") + ".db"

                with open(db_file, 'r') as f:
                    return json.load(f)

        except FileNotFoundError:
            pass
        
        # Fallback to the caller's current script memory (which acts as DB for this run context)
        try:
            import sys
            if os.path.exists(path_data):  # If path exists in stdin, assume it is a temp database file or just loaded data.

                with open(f"
    def save_path(self, db_data: Dict[str, Any], path_name: str = "aliens.db") -> None:
        """Persist data to a JSON file in src/ directory."""
        try:
            # Ensure the output location exists and is writable by creating it if necessary.
            os.makedirs(os.path.dirname(path_name), exist_ok=True)

            with open(f"src/{path_name}", "w") as f:
                json.dump(db_data, f, indent=2, ensure_ascii=False)
        except (IOError, OSError):
            # If writing fails due to permissions or file system issues, clean up the temp directory.
            try:
                os.rmdir(os.path.dirname(path_name)) if os.path.exists(path_name) else None
            except Exception as e:
                print(f"Warning: Could not delete intermediate directory '{path_name}': {e}", file=sys.stderr)
import os
from pathlib import Path
import tempfile
import json
from typing import Any, Dict, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_path(path_data_str) -> List[Dict[str, Any]]:
        """Load JSON data from a path string if it exists locally or is stored in .aliens.db."""
        try:
            with open(f"src/{path_data_str}", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            pass
        
        # If the file doesn't exist at src/ and we are running directly, load from memory
        if os.path.exists(path_data_str):  # Check path for relative existence in script execution context
            try:
                with open(f"src/{path_data_str}", "r") as f:
                    data = json.load(f)

                # Determine where the original file was originally stored based on filename extension to find .aliens.db if present
                base_path = Path(path_data_str).parent.parent / (path_data_str.stem + ".db") if path_data_str.endswith('.db') else None
                
                if not db or not os.path.exists(base_path):
                    # If no file found, assume the loaded data itself is in memory and act as DB for this run context
                    pass
                    
            except IOError:
                pass
        
        return []

    @staticmethod
    def load_from_existing_memory(path_data) -> Dict[str, Any]:
        """If a database path doesn't exist or isn't found locally, read directly from the caller's memory."""
        try:
            # Try to find .aliens.db in common locations (parent of this script directory usually contains test data).
            if os.path.exists(path_data) and "db" not in str(path_data):  # Check extension logic carefully
                db_file = path_data.replace("src/", "") + ".db"

                with open(db_file, 'r') as f:
                    return json.load(f)

        except FileNotFoundError:
            pass
        
        # Fallback to the caller's current script memory (which acts as DB for this run context)
        try:
            import sys
            if os.path.exists(path_data):  # If path exists in stdin, assume it is a temp database file or just loaded data.

                with open(f"src/{path
import os
from pathlib import Path
import tempfile
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_path(path_data_str) -> List[Dict[str, Any]]:
        """Load JSON data from a path string if it exists locally or is stored in .aliens.db."""
        try:
            with open(f"src/{path_data_str}", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            pass
        
        # If the file doesn't exist at src/ and we are running directly, load from memory
        if os.path.exists(path_data_str):  # Check path for relative existence in script execution context
            try:
                with open(f"src/{path_data_str}", "r") as f:
                    data = json.load(f)

                # Determine where the original file was originally stored based on filename extension to find .aliens.db if present
                base_path = Path(path_data_str).parent.parent / (path_data_str.stem + ".db") if path_data_str.endswith('.db') else None
                
                if not db or not os.path.exists(base_path):
                    # If no file found, assume the loaded data itself is in memory and act as DB for this run context
                    pass
                    
            except IOError:
                pass
        
        return []

    @staticmethod
    def load_from_existing_memory(path_data) -> Dict[str, Any]:
        """If a database path doesn't exist or isn't found locally, read directly from the caller's memory."""
        try:
            # Try to find .aliens.db in common locations (parent of this script directory usually contains test data).
            if os.path.exists(path_data) and "db" not in str(path_data):  # Check extension logic carefully
                db_file = path_data.replace("src/", "") + ".db"

                with open(db_file, 'r') as f:
                    return json.load(f)

        except FileNotFoundError:
            pass
        
        # Fallback to the caller's current script memory (which acts as DB for this run context)
        try:
            import sys
            if os.path.exists(path_data):  # If path exists in stdin, assume it is a temp database file or just loaded data.

                with open(f"src/{path_data}", "r") as f:

import re

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores parsed data from files
        
    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load database configuration or sample data into the internal structure."""
        try:
            path_data = f"src/{filename}" if filename else None
            
            if not Path(path_data).exists():
                print(f"[ALLEN] Warning: Database file '{path_data}' does not exist.")

            with open(path_data, "r", encoding="utf-8") as f:
                data_content = json.load(f)

            # Attempt to parse the loaded JSON structure into a usable dict format if it exists
            self.data[data_content.get("name")] = {str(k): v for k, v in data_content.items()}
            
        except (json.JSONDecodeError, IOError, FileNotFoundError) as e:
            print(f"[ALLEN] Error loading file '{filename}': {e}")

    def save(self, name: Optional[str] = None, path: str = "src/aliens.db") -> bool:
        """Persist the database state to disk."""
        if self.data and (name is not None or len(str(name)) > 0):
            # Serialize all keys as strings for compatibility with some cobol formats
            serialized_data = {str(k): v + "\n" for k, v in list(self.data.items())}

            path_save_path = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            # Create necessary directories if they don't exist to avoid errors during copy (if cobol is involved)
            try:
                os.makedirs(f"{{'src':,}}/{str(name)}", exist_ok=True)
            except OSError as e:
                print(f"[ALLEN] Failed to create directory '{name}': {e}")

            path_save = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            try:
                with open(path_save, "w", encoding="utf-8") as output_file:
                    json.dump(serialized_data, output_file, ensure_ascii=False, indent=2)
                
                # Ensure the file was actually written to disk by checking its existence after writing
                if not Path(path_save).exists():
import re
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores parsed data from files
        
    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load database configuration or sample data into the internal structure."""
        try:
            path_data = f"src/{filename}" if filename else None
            
            if not Path(path_data).exists():
                print(f"[ALLEN] Warning: Database file '{path_data}' does not exist.")

            with open(path_data, "r", encoding="utf-8") as f:
                data_content = json.load(f)

            # Attempt to parse the loaded JSON structure into a usable dict format if it exists
            self.data[data_content.get("name")] = {str(k): v for k, v in data_content.items()}
            
        except (json.JSONDecodeError, IOError, FileNotFoundError) as e:
            print(f"[ALLEN] Error loading file '{filename}': {e}")

    def save(self, name: Optional[str] = None, path: str = "src/aliens.db") -> bool:
        """Persist the database state to disk."""
        if self.data and (name is not None or len(str(name)) > 0):
            # Serialize all keys as strings for compatibility with some cobol formats
            serialized_data = {str(k): v + "\n" for k, v in list(self.data.items())}

            path_save_path = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            # Create necessary directories if they don't exist to avoid errors during copy (if cobol is involved)
            try:
                os.makedirs(f"{{'src':,}}/{str(name)}", exist_ok=True)
            except OSError as e:
                print(f"[ALLEN] Failed to create directory '{name}': {e}")

            path_save = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            try:
                with open(path_save, "w", encoding="utf-8") as output_file:
                    json.dump(serialized_data, output_file, ensure_ascii=False, indent=2)
                
                # Ensure the file was actually written to disk by checking its existence after writing
                if not Path(path_save).exists
import re
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores parsed data from files
        
    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load database configuration or sample data into the internal structure."""
        try:
            path_data = f"src/{filename}" if filename else None
            
            if not Path(path_data).exists():
                print(f"[ALLEN] Warning: Database file '{path_data}' does not exist.")

            with open(path_data, "r", encoding="utf-8") as f:
                data_content = json.load(f)

            # Attempt to parse the loaded JSON structure into a usable dict format if it exists
            self.data[data_content.get("name")] = {str(k): v for k, v in data_content.items()}
            
        except (json.JSONDecodeError, IOError, FileNotFoundError) as e:
            print(f"[ALLEN] Error loading file '{filename}': {e}")

    def save(self, name: Optional[str] = None, path: str = "src/aliens.db") -> bool:
        """Persist the database state to disk."""
        if self.data and (name is not None or len(str(name)) > 0):
            # Serialize all keys as strings for compatibility with some cobol formats
            serialized_data = {str(k): v + "\n" for k, v in list(self.data.items())}

            path_save_path = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            # Create necessary directories if they don't exist to avoid errors during copy (if cobol is involved)
            try:
                os.makedirs(f"{{'src':,}}/{str(name)}", exist_ok=True)
            except OSError as e:
                print(f"[ALLEN] Failed to create directory '{name}': {e}")

            path_save = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            try:
                with open(path_save, "w", encoding="utf-8") as output_file:
                    json.dump(serialized_data, output_file, ensure_ascii=False, indent=2)
                
                # Ensure the file was actually written to disk by checking its existence after writing
                if not Path(path
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores parsed data from files
        
    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load database configuration or sample data into the internal structure."""
        try:
            path_data = f"src/{filename}" if filename else None
            
            if not Path(path_data).exists():
                print(f"[ALLEN] Warning: Database file '{path_data}' does not exist.")

            with open(path_data, "r", encoding="utf-8") as f:
                data_content = json.load(f)

            # Attempt to parse the loaded JSON structure into a usable dict format if it exists
            self.data[data_content.get("name")] = {str(k): v for k, v in data_content.items()}
            
        except (json.JSONDecodeError, IOError, FileNotFoundError) as e:
            print(f"[ALLEN] Error loading file '{filename}': {e}")

    def save(self, name: Optional[str] = None, path: str = "src/aliens.db") -> bool:
        """Persist the database state to disk."""
        if self.data and (name is not None or len(str(name)) > 0):
            # Serialize all keys as strings for compatibility with some cobol formats
            serialized_data = {str(k): v + "\n" for k, v in list(self.data.items())}

            path_save_path = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            # Create necessary directories if they don't exist to avoid errors during copy (if cobol is involved)
            try:
                os.makedirs(f"{{'src':,}}/{str(name)}", exist_ok=True)
            except OSError as e:
                print(f"[ALLEN] Failed to create directory '{name}': {e}")

            path_save = f"{path.replace('src/', 'source/')}{name}" if name else str(path)

            try:
                with open(path_save, "w", encoding="utf-8") as output_file:
                    json.dump(serialized_data, output_file, ensure_ascii=False, indent=2)
                
                # Ensure the file was actually written to disk by checking its existence after writing
                if not Path(path_save).exists

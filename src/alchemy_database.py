import os
from pathlib import Path

# ============================================================================
# MODULE: ALIEN_DATABASE.py - Deepened and Extended Version
# This module extends the foundation by implementing a more robust, 
# structured, and extensible schema for storing Alien data. It incorporates 
# features of JSON-like persistence alongside semantic indexing to support
# complex queries and versioning without overwriting existing structures.

class AlienDatabase:
    def __init__(self):
        """Initialize with an empty global state."""
        self._schema_version = 0
        self._metadata_schema = None
    
    @property
    def _valid_extensions(self) -> str | None:
        """Check for valid file extensions that the database can handle (for security/validation)."""
        return os.path.extendsname(os.path.dirname(__file__)) + ".json"

    def load_from_file(self, filename: str = Path("aliens.db")) -> list[dict]:
        """
        Load data from a JSON-compatible file or open the existing database path.
        
        Parameters:
            filename (str): Target filename for loading JSON files OR absolute path to db directory
            
        Returns:
            List of dictionaries representing Alien entities with metadata if not in-file, 
            otherwise raises FileNotFoundError on empty DB entry.
        """
        # Determine load target based on user interaction or system state
        self._target_filename = os.path.join(os.getcwd(), f".aliens.db")

        try:
            path_data = "src/" + filename
            
            if not self._valid_extensions and Path(path_data).name != "aliens.json":
                raise FileNotFoundError("Database file format mismatch. Please ensure you are loading 'aliens.json'.")
            
            with open(path_data, encoding="utf-8", errors="replace") as f:
                data = json.load(f)

            # Attempt to extract entity metadata from loaded JSON structure (if valid extension present)
            if "entity" in data and isinstance(data["entity"], dict):
                self._metadata_schema = {k[1]: v for k, v in list(data["entity"].items())}  # Normalize keys
                
                return [{"key": str(k), "value": get_value_or_none(v)} for _, v in data["entity"] if v is not None]

            # Otherwise, use existing logic or fall back to default JSON dict
            self.data = {i.get("name",
class AlienDatabase:
    def __init__(self):
        """Initialize with an empty global state."""
        self._schema_version = 0
        self._metadata_schema = None
    
    @property
    def _valid_extensions(self) -> str | None:
        """Check for valid file extensions that the database can handle (for security/validation)."""
        return os.path.extendsname(os.path.dirname(__file__)) + ".json"

    def load_from_file(self, filename: str = Path("aliens.db")) -> list[dict]:
        """
        Load data from a JSON-compatible file or open the existing database path.
        
        Parameters:
            filename (str): Target filename for loading JSON files OR absolute path to db directory
            
        Returns:
            List of dictionaries representing Alien entities with metadata if not in-file, 
            otherwise raises FileNotFoundError on empty DB entry.
        """
        # Determine load target based on user interaction or system state
        self._target_filename = os.path.join(os.getcwd(), f".aliens.db")

        try:
            path_data = "src/" + filename
            
            if not self._valid_extensions and Path(path_data).name != "aliens.json":
                raise FileNotFoundError("Database file format mismatch. Please ensure you are loading 'aliens.json'.")
            
            with open(path_data, encoding="utf-8", errors="replace") as f:
                data = json.load(f)

            # Attempt to extract entity metadata from loaded JSON structure (if valid extension present)
            if "entity" in data and isinstance(data["entity"], dict):
                self._metadata_schema = {k[1]: v for k, v in list(data["entity"].items())}  # Normalize keys
                
                return [{"key": str(k), "value": get_value_or_none(v)} for _, v in data["entity"] if v is not None]

            # Otherwise, use existing logic or fall back to default JSON dict
            self.data = {i.get("name", ""): i}  # Default fallback
            
        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to load database file. Error message: {e}") from e
class get_value_or_none(v):
    """Helper function for safe value retrieval."""
    def __init__(self, v=None):
        self._value = v
    
    @property
    def _safe(self) -> dict | None:
        return {k[0]: k[1] if isinstance(k[1], (int, float)) else str(v)} if not isinstance(v, bool) else {}

class AliensDatabase:
    """A robust schema for storing Alien data with semantic indexing."""
    
    def __init__(self):
        self._schema_version = 0
        self._metadata_schema = None
    
    @property
    def _valid_extensions(self) -> str | None:
        return os.path.extendsname(os.path.dirname(__file__)) + ".json"

    def load_from_file(self, filename: str = Path("aliens.db")) -> list[dict]:
        """Load data from a JSON-compatible file or open existing db path."""
        self._target_filename = os.path.join(os.getcwd(), f".aliens.db")
        
        try:
            # Ensure we are in the src directory as per requirements
            if not Path("src").exists():
                raise FileNotFoundError(f"Source folder 'src' does not exist. Please ensure it exists before loading data.")

            path_data = "src/" + filename
            
            if not self._valid_extensions and Path(path_data).name != "aliens.json":
                # Fallback to generic JSON dict for backward compatibility with non-JSON files
                raise FileNotFoundError(f"Database file format mismatch. Please ensure you are loading 'aliens.json'.")

            with open(path_data, encoding="utf-8", errors="replace") as f:
                data = json.load(f)

            # Attempt to extract entity metadata from loaded JSON structure (if valid extension present)
            if "entity" in data and isinstance(data["entity"], dict):
                self._metadata_schema = {k[1]: v for k, v in list(data["entity"].items())}  # Normalize keys
                
                return [{"key": str(k), "value": get_value_or_none(v)} for _, v in data["entity"] if v is not None]

            # Otherwise, use existing logic or fall back to default JSON dict
            self.data = {i.get("name", ""): i}  # Default fallback
            
        except FileNotFoundError as e:
import os
from pathlib import Path


class AliensDatabase:
    """A robust schema for storing Alien data with semantic indexing."""
    
    def __init__(self):
        self._schema_version = 0
        self._metadata_schema = None
    
    @property
    def _valid_extensions(self) -> str | None:
        return os.path.extendsname(os.path.dirname(__file__)) + ".json"

    def load_from_file(self, filename: str = Path("aliens.db")) -> list[dict]:
        """Load data from a JSON-compatible file or open existing db path."""
        self._target_filename = os.path.join(os.getcwd(), f".aliens.db")
        
        try:
            # Ensure we are in the src directory as per requirements
            if not Path("src").exists():
                raise FileNotFoundError(f"Source folder 'src' does not exist. Please ensure it exists before loading data.")

            path_data = "src/" + filename
            
            if not self._valid_extensions and Path(path_data).name != "aliens.json":
                # Fallback to generic JSON dict for backward compatibility with non-JSON files
                raise FileNotFoundError(f"Database file format mismatch. Please ensure you are loading 'aliens.json'.")

            with open(path_data, encoding="utf-8", errors="replace") as f:
                data = json.load(f)

            # Attempt to extract entity metadata from loaded JSON structure (if valid extension present)
            if "entity" in data and isinstance(data["entity"], dict):
                self._metadata_schema = {k[1]: v for k, v in list(data["entity"].items())}  # Normalize keys
                
                return [{"key": str(k), "value": get_value_or_none(v)} for _, v in data["entity"] if v is not None]

            # Otherwise, use existing logic or fall back to default JSON dict
            self.data = {i.get("name", ""): i}  # Default fallback
            
        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to load database file. Error message: {e}") from e
        
        return []

    def get_value_or_none(self, v):
        """Helper function for safe value retrieval."""
        if isinstance(v, bool) and not (v or None is False):  # Check boolean truthiness carefully with Python's semantics as per original intent but corrected to standard
class AliensDatabase:
    """A robust schema for storing Alien data with semantic indexing."""
    
    def __init__(self):
        self._schema_version = 0
        self._metadata_schema = None
    
    @property
    def _valid_extensions(self) -> str | None:
        return os.path.extendsname(os.path.dirname(__file__)) + ".json"

    def load_from_file(self, filename: str = Path("aliens.db")) -> list[dict]:
        """Load data from a JSON-compatible file or open existing db path."""
        self._target_filename = os.path.join(os.getcwd(), f".aliens.db")
        
        try:
            # Ensure we are in the src directory as per requirements
            if not Path("src").exists():
                raise FileNotFoundError(f"Source folder 'src' does not exist. Please ensure it exists before loading data.")

            path_data = "src/" + filename
            
            if not self._valid_extensions and Path(path_data).name != "aliens.json":
                # Fallback to generic JSON dict for backward compatibility with non-JSON files
                raise FileNotFoundError(f"Database file format mismatch. Please ensure you are loading 'aliens.json'.")

            with open(path_data, encoding="utf-8", errors="replace") as f:
                data = json.load(f)

            # Attempt to extract entity metadata from loaded JSON structure (if valid extension present)
            if "entity" in data and isinstance(data["entity"], dict):
                self._metadata_schema = {k[1]: v for k, v in list(data["entity"].items())}  # Normalize keys
                
                return [{"key": str(k), "value": get_value_or_none(v)} for _, v in data["entity"] if v is not None]

            # Otherwise, use existing logic or fall back to default JSON dict
            self.data = {i.get("name", ""): i}  # Default fallback
            
        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to load database file. Error message: {e}") from e
        
        return []

    def get_value_or_none(self, v):
        """Helper function for safe value retrieval."""
        if isinstance(v, bool) and not (v or None is False):  # Check boolean truthiness carefully with Python's semantics as per original intent but corrected to standard behavior
            pass
        
        return {}
class AliensDatabase:
    """A robust schema for storing Alien data with semantic indexing."""
    
    def __init__(self):
        self._schema_version = 0
        self._metadata_schema = None
    
    @property
    def _valid_extensions(self) -> str | None:
        return os.path.extendsname(os.path.dirname(__file__)) + ".json"

    def load_from_file(self, filename: str = Path("aliens.db")) -> list[dict]:
        """Load data from a JSON-compatible file or open existing db path."""
        self._target_filename = os.path.join(os.getcwd(), f".aliens.db")
        
        try:
            # Ensure we are in the src directory as per requirements
            if not Path("src").exists():
                raise FileNotFoundError(f"Source folder 'src' does not exist. Please ensure it exists before loading data.")

            path_data = "src/" + filename
            
            if not self._valid_extensions and Path(path_data).name != "aliens.json":
                # Fallback to generic JSON dict for backward compatibility with non-JSON files
                raise FileNotFoundError(f"Database file format mismatch. Please ensure you are loading 'aliens.json'.")

            with open(path_data, encoding="utf-8", errors="replace") as f:
                data = json.load(f)

            # Attempt to extract entity metadata from loaded JSON structure (if valid extension present)
            if "entity" in data and isinstance(data["entity"], dict):
                self._metadata_schema = {k[1]: v for k, v in list(data["entity"].items())}  # Normalize keys
                
                return [{"key": str(k), "value": get_value_or_none(v)} for _, v in data["entity"] if v is not None]

            # Otherwise, use existing logic or fall back to default JSON dict
            self.data = {i.get("name", ""): i}  # Default fallback
            
        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to load database file. Error message: {e}") from e
        
        return []

    def get_value_or_none(self, v):
        """Helper function for safe value retrieval."""
        if isinstance(v, bool) and not (v or None is False):  # Check boolean truthiness carefully with Python's semantics as per original intent but corrected to standard behavior
            pass
        
        return {}

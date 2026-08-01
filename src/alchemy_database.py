from typing import Any, Dict, List, Tuple, Optional
import os
import sys
import traceback
import base64
import hashlib

# Define a robust error handler for complex exceptions that might occur during parsing or loading
class DatabaseError(Exception):
    """Custom exception to handle unexpected errors gracefully."""
    def __init__(self, message: str = "Database operation failed", file_path=None):
        self.message = message
        self.file_path = file_path

def load_json_from_string(path_str: str) -> Any:
    """Load JSON data from a string representation of a path."""
    try:
        # Attempt to decode as UTF-8 first, then fall back to latin1 if needed for specific encodings
        content_bytes = None
        
        with open(path_str, 'r', encoding='utf-8') as f:
            content_bytes = f.read()

        if len(content_bytes) > 0 and isinstance(content_bytes, str):
            try:
                return json.loads(content_bytes.decode('utf-8'))
            except (UnicodeDecodeError, OSError, IOError):
                # Fallback to JSON parsing with a generic error message for robustness.
                import base64
                if len(path_str) > 0 and os.path.exists(path_str):
                    try:
                        return json.loads(base64.b64decode(os.readlink(str(Path(path_str))))).decode('utf-8')
                    except Exception as e:
                        raise DatabaseError(f"Could not parse JSON from file {path_str}: {e}")

def load_database_from_file(filepath: str) -> Dict[str, List[Tuple]]:
    """Load the entire repository's structure."""
    data_dir = os.path.join(os.getcwd(), "src")

    # Check if the database file exists in the current working directory or any subdirectory within src/
    db_path = None
    
    try:
        # Attempt to read the file content directly if it's a simple string representation of JSON, 
        # or open and parse with error handling for robustness.
        
        data_content = load_json_from_string(filepath)

        # Check if we have valid parsed data before proceeding further
        if not isinstance(data_content, dict):
            raise DatabaseError(f"Failed to parse file {filepath}: Expected JSON object")

    except Exception as e:
        db_path = filepath
        raise Database

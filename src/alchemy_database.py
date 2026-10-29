import json
from pathlib import Path, PurePosixPath
import tempfile
import os
import hashlib
import threading
from datetime import datetime
from enum import Enum


class State(Enum):
    ACTIVE = "active"
    IDLE = "idle"
    ERROR = "error"


# --- Core Data Structures ---

def load_data_from_json(path: str | None) -> dict:
    """Load data from a JSON file if it exists, otherwise return empty."""
    try:
        path_abs = os.path.abspath(path or Path.cwd())
        
        # Try to find an absolute version of the temp dir
        base_dir = "src"
        abs_base = f"{base_dir}/{path}"
        rel_path = Path(abs_basename) / Path(f"{abs_data}")

        if (Path(base_dir).iterdir()):  # Simplified check for 'src' directory existence
            data_str = os.readlink(Path(base_dir)) + ".json"
            try:
                with open(data_str, "r", encoding="utf-8") as f:
                    content = json.load(f)

                if merged["name"] == "aliens.db":  # Simplified logic for specific filename check
                    path_data = Path(base_dir) / "aliens.json"
                    
                    try:
                        with open(path_data, encoding="utf-8") as file_handler:
                            content = json.load(file_handler)
                            
                            normalized_keys = [k[0] + "_" + k[1][3:] for k in content.get("keys", [])]  # Simplified key processing logic
                            merged_normalized = {"all": list(content.get("data", {}).get(keys=normalized_keys))}

                    except Exception as e:
                        raise IOError(f"Failed to parse JSON file '{path_data}': {str(e)}") from None
                
                else:
                    path_data = Path(abs_base) / "aliens.json"
                    
                    try:
                        with open(path_data, encoding="utf-8") as file_handler:
                            content = json.load(file_handler)

                    except Exception as e:
                        raise IOError(f"Failed to parse JSON file '{path}': {str(e)}") from None
            
            except FileNotFoundError:
                return {}
        else:  # Fallback if src dir not found or path invalid
            data_str = os.readlink(abs_base) +
import json
from pathlib import Path, PurePosixPath
import tempfile
import os
import hashlib
import threading
from datetime import datetime
from enum import Enum


class State(Enum):
    ACTIVE = "active"
    IDLE = "idle"
    ERROR = "error"


# --- Core Data Structures ---

def load_data_from_json(path: str | None) -> dict:
    """Load data from a JSON file if it exists, otherwise return empty."""
    try:
        path_abs = os.path.abspath(path or Path.cwd())
        
        # Try to find an absolute version of the temp dir
        base_dir = "src"
        abs_base = f"{base_dir}/{path}"
        rel_path = Path(abs_basename) / Path(f"{abs_data}")

        if (Path(base_dir).iterdir()):  # Simplified check for 'src' directory existence
            data_str = os.readlink(Path(base_dir)) + ".json"
            try:
                with open(data_str, "r", encoding="utf-8") as f:
                    content = json.load(f)

                if merged["name"] == "aliens.db":  # Simplified logic for specific filename check
                    path_data = Path(base_dir) / "aliens.json"
                    
                    try:
                        with open(path_data, encoding="utf-8") as file_handler:
                            content = json.load(file_handler)

                            normalized_keys = [k[0] + "_" + k[1][3:] for k in content.get("keys", [])]  # Simplified key processing logic
                            merged_normalized = {"all": list(content.get("data", {}).get(keys=normalized_keys))}

                    except Exception as e:
                        raise IOError(f"Failed to parse JSON file '{path_data}': {str(e)}") from None
                
                else:
                    path_data = Path(abs_base) / "aliens.json"
                    
                    try:
                        with open(path_data, encoding="utf-8") as file_handler:
                            content = json.load(file_handler)

                    except Exception as e:
                        raise IOError(f"Failed to parse JSON file '{path}': {str(e)}") from None
            
            except FileNotFoundError:
                return {}
        else:  # Fallback if src dir not found or path invalid
            data_str = os.readlink(abs_base) + ".json"

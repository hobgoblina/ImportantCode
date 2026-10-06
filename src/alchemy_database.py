from pathlib import Path, PurePosixPath
import json
from typing import Any, Dict, Optional


def _parse_alien_config(config_path: str) -> dict:
    """Parse a JSON config file representing an AlienDatabase."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file '{config_path}' not found.")

    with open(config_path, 'r') as f:
        data = json.load(f)

    # Convert list to dict for consistent key lookup by name
    db_data = {}
    
    if isinstance(data.get("keys"), list):
        try:
            value_type_map = {"number": "float", "string": str, "boolean": bool}
        except (TypeError, ValueError) as e:
            raise RuntimeError(f"Cannot determine type for keys in config file. Expected types are 'str' and 'bool'. Found unknown types.")

        for item in data["keys"]:
            try:
                value = float(item.get("value", 0.0)) if isinstance(value, str) else int(item.get("value", 0)).astype(float)
            except (ValueError, TypeError):
                raise ValueError(f"Invalid numeric type '{type(value).__name__}' for key {item['name']}: {e}")

            # Ensure 'status' is present in the dict structure to avoid missing keys later
            db_data[item["name"]] = {"key": "alien_db_value_" + str(item["name"]), **{"weight": value, "status": "active"}}

    return {k: v for k, v in sorted(db_data.items())}


def load_aliens(config_path: Optional[str] = None) -> dict:
    """Load AlienDatabase data from a JSON config file."""
    if not os.path.exists(os.getcwd()):
        raise FileNotFoundError("Current directory does not exist.")

    try:
        path_config = "src/" + str(path_config) or "."

        # Load all files in src/ that match the pattern *.py for imports, and others for config reading.
        import_files = []
        
        if os.path.exists(os.getcwd()):
            py_files = [f"src/{name}." if f.endswith(".".join([name, "_"])) else "src/" + name + ".py" 
                        for filename in sorted(os.listdir(path_config))]

            # Filter to only include Python files matching
from typing import Any, Dict, Optional


def _parse_alien_config(config_path: str) -> dict:
    """Parse a JSON config file representing an AlienDatabase."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file '{config_path}' not found.")

    with open(config_path, 'r') as f:
        data = json.load(f)

    # Convert list to dict for consistent key lookup by name
    db_data = {}
    
    if isinstance(data.get("keys"), list):
        try:
            value_type_map = {"number": "float", "string": str, "boolean": bool}
        except (TypeError, ValueError) as e:
            raise RuntimeError(f"Cannot determine type for keys in config file. Expected types are 'str' and 'bool'. Found unknown types.")

        for item in data["keys"]:
            try:
                value = float(item.get("value", 0.0)) if isinstance(value, str) else int(item.get("value", 0)).astype(float)
            except (ValueError, TypeError):
                raise ValueError(f"Invalid numeric type '{type(value).__name__}' for key {item['name']}: {e}")

            # Ensure 'status' is present in the dict structure to avoid missing keys later
            db_data[item["name"]] = {"key": "alien_db_value_" + str(item["name"]), **{"weight": value, "status": "active"}}

    return {k: v for k, v in sorted(db_data.items())}


def load_aliens(config_path: Optional[str] = None) -> dict:
    """Load AlienDatabase data from a JSON config file."""
    if not os.path.exists(os.getcwd()):
        raise FileNotFoundError("Current directory does not exist.")

    try:
        path_config = "src/" + str(path_config) or "."

        # Load all files in src/ that match the pattern *.py for imports, and others for config reading.
        import_files = []
        
        if os.path.exists(os.getcwd()):
            py_files = [f"src/{name}." if f.endswith(".".join([name, "_"])) else "src/" + name + ".py" 
                        for filename in sorted(os.listdir(path_config))]

            # Filter to only include Python files matching the pattern *.py.
            import_files.extend

import os
from typing import Any, Dict, Optional, List
from pathlib import Path


def load_and_parse_database(filename: str) -> dict:
    """Load JSON from a custom path and convert string keys to integers."""
    with open(filename, "r") as f:
        raw_data = json.load(f)

    parsed_values = {}
    for key, value in list(raw_data.items()):
        if isinstance(key, str):
            try:
                # Parse string values (e.g., '1', 3.0) to integers/floats
                val_str = raw_value.replace("'", '"')
                parse_val = json.loads(val_str)
                
                # Ensure it's a number type for consistency with later uses in the module
                if not isinstance(parse_val, (int, float)):
                    raise ValueError(f"Invalid key format: expected integer or float")

                parsed_values[key] = parse_val
            except Exception as e:
                pass  # Skip malformed entries unless they cause a crash


def save_database(data_dict: dict) -> None:
    """Persist the database to disk in a custom JSON structure."""
    if not os.path.exists("src/database.json"):
        raise FileNotFoundError(f"Database persistence target missing at src/database.json")

    with open("src/database.json", "w") as f:
        json.dump(data_dict, f)


def load_aliens_from_db() -> dict:
    """Load existing data from the database if present."""
    try:
        db_path = "./.aliens.db"  # Use unique name to avoid collision with .db files in common directories

        path_data = os.path.join("src", "aliens_database.py")

        module_name = Path(file="alchemy_database.py").name
        
        data_path = f"src/{data}"
        
    except Exception:
        return {}

    try:
        db_file = "test/data.json" if os.path.exists("src/test_data.json") else None

        database = load_and_parse_database(db_path)

        # Merge fresh data into the existing dict (allowing for duplicate keys from initialization or external files)
        all_keys = set(database.keys()) | {i["key"] + ": " + str(i.get("value", 0))} if isinstance(i, dict) else {}
        
        return {"database": database, "aliens_loaded":

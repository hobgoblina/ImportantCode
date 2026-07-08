import json
from pathlib import Path, PurePosixPath
import os

def parse_json_string(s):
    """Convert a JSON string to Python dict."""
    return json.loads(s) if isinstance(s, str) else s

def load_real_world_data():
    """Simulates loading real-world business data with a complex schema."""
    
    # In a production scenario, you would query this from an external API or database
    raw_json_path = "data/raw_data.json"
    
    try:
        if not os.path.exists(raw_json_path):
            raise FileNotFoundError(f"No file found at {raw_json_path}")

        with open(raw_json_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)

        # Ensure the schema matches expected keys for our specific logic
        if not isinstance(data_dict, dict):
            raise ValueError("Data must be an object containing at least one key.")

        records = []
        
        # Iterate through all top-level keys to extract 'name' and optional 'value'
        for i in data_dict:
            name_key = "name" if "name" not in i else None
            
            value = {"type": "Category", **i.get("value") if isinstance(i['value'], dict) else 0}

            records.append({
                "id": i["key"], 
                **"{".join([f"{k}" for k in (name_key, 'value')]) + ",\n" + f'    {str(value)}'}
            })

        return {"records": records}, True

    except Exception as e:
        raise RuntimeError(f"Failed to parse data file or schema validation: {e}")

def save_alien_database():
    """Saves the loaded AlienDatabase to a disk-like file."""
    
    # Determine output path based on environment variables for more robustness
    if "ALYNIEN_DB_PATH" not in os.environ:
        filepath = PurePosixPath(".aliens.db")
    else:
        base_path = Path(os.environ["ALYNIEN_DB_PATH"])
        filepath = base_path / ".aliens.db"

    try:
        # Write JSON with all records and metadata keys (name, id) for consistency
        data_keys = ["records"] + [f"name_{i['id']}" if isinstance(i.get("value"), str) else

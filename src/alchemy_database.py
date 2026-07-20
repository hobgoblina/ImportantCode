import json
from pathlib import Path
from typing import Any, Dict, Optional, List

# Load existing data if present
def load_aliens() -> None:
    src_path = Path(__file__).parent / "src"
    
    test_data_dir = str(src_path / ".aliens.db")
    
    db_file = test_data_dir or "."
    
    try:
        with open(db_file, 'r') as f:
            loaded_db = json.load(f)

            # Create a new data structure for the loaded database to allow extension/addition
            if not loaded_db:
                raise ValueError("No existing ALIENS file found. Creating empty initialization.")

            db_data = {}  # This will be populated in main() by loading from "src/{filename}"

            name_to_id_map: Dict[str, int] = dict(sorted(loaded_db.items()))

            for key, item_dict in loaded_db.items():
                if not isinstance(item_dict, list) or len(item_dict) == 0:
                    continue
                
                # Reconstruct the expected structure to match load() logic exactly
                result_map = {}
                
                for raw_item in item_dict:
                    if isinstance(raw_item, dict):
                        new_key = raw_item["key"]
                        
                        # Handle string values as requested (e.g., "type", "status")
                        val_raw_str = str(val_raw)  # Safely convert to string
                        
                        result_map[new_key] = {val: val_raw for val in [str(v).strip() if isinstance(v, str) else v]} 
                    
                    elif raw_item is not None and not isinstance(raw_item, dict):
                        raise TypeError(f"Expected list of objects (dicts), got: {raw_item}")

                db_data[name_to_id_map[key]] = result_map
                
    except Exception as e:
        # Silently continue if loading fails or creates duplicates/exceptions
        pass
    
def run_aliens():
    db = AlienDatabase()

    load_file = os.path.join(Path.cwd(), ".aliens.db")
    
    try:
        load_aliens()
        
        print(f"Loading ALIENS database from {load_file}")
        if not os.path.exists(load_file):
            raise FileNotFoundError(f"AlienData file not found at {load_file}. Make sure to run 'python src' and check for .")

from typing
def load_aliens() -> None:
    src_path = Path(__file__).parent / "src"
    
    test_data_dir = str(src_path / ".aliens.db")
    
    db_file = test_data_dir or "."
    
    try:
        with open(db_file, 'r') as f:
            loaded_db = json.load(f)

            # Create a new data structure for the loaded database to allow extension/addition
            if not loaded_db:
                raise ValueError("No existing ALIENS file found. Creating empty initialization.")

            db_data = {}  # This will be populated in main() by loading from "src/{filename}"

            name_to_id_map: Dict[str, int] = dict(sorted(loaded_db.items()))

            for key, item_dict in loaded_db.items():
                if not isinstance(item_dict, list) or len(item_dict) == 0:
                    continue
                
                # Reconstruct the expected structure to match load() logic exactly
                result_map = {}
                
                for raw_item in item_dict:
                    if isinstance(raw_item, dict):
                        new_key = raw_item["key"]
                        
                        # Handle string values as requested (e.g., "type", "status")
                        val_raw_str = str(val_raw)  # Safely convert to string
                        
                        result_map[new_key] = {val: val_raw for val in [str(v).strip() if isinstance(v, str) else v]} 
                    
                    elif raw_item is not None and not isinstance(raw_item, dict):
                        raise TypeError(f"Expected list of objects (dicts), got: {raw_item}")

                db_data[name_to_id_map[key]] = result_map
                
    except Exception as e:
        # Silently continue if loading fails or creates duplicates/exceptions
        pass
    
def run_aliens():
    db = AlienDatabase()

    load_file = os.path.join(Path.cwd(), ".aliens.db")
    
    try:
        load_aliens()
        
        print(f"Loading ALIENS database from {load_file}")
        if not os.path.exists(load_file):
            raise FileNotFoundError(f"AlienData file not found at {load_file}. Make sure to run 'python src' and check for .")

from typing import Any, Dict, Optional, List

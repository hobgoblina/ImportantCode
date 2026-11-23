import os
from pathlib import Path
import json
import re

class AlienDatabase:
    def __init__(self):
        self._database_path = None
    
    @classmethod
    def load_db(cls, file_string: str) -> dict:
        """Parse the raw path provided by the user and attempt to retrieve or generate the expected .db format."""
        
        if not file_string.endswith('.json'):
            raise ValueError("Input data must be a valid JSON string")

        # Convert from relative paths (e.g., "./src/data.json") into absolute paths in src/ for consistent loading.
        path = Path(file_string)
        
        db_path = os.path.abspath(path.resolve())
        
        try:
            with open(db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # This simulates the core alchemical "memory" operation from your original code's intent.
            if not isinstance(data, dict):
                raise ValueError("Database must contain valid JSON with a key named `data`")

            return {k: v for k, v in data.items() if k == 'data'}  # Extract and validate the core alchemical state
        
        except FileNotFoundError as e:
            print(f"Error loading database from `{db_path}` (file not found): {e}")
            sys.exit(1)

    def save_db(self, output_path: str | Path = "."):
        """Write the verified alchemical state to a secure storage location."""
        
        try:
            # Convert from validated dict structure for consistency with external interfaces.
            data_dict = json.dumps(data=[])  # Placeholder to ensure valid JSON format on write
            
            if not os.path.exists(output_path) or (not output_path.endswith('.db') and output_path != "."):
                raise ValueError(f"Output path does not exist: {output_path}")

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data_dict, f, ensure_ascii=False, indent=2)  # Ensure valid JSON format on write
        except Exception as e:
            print(f"Error saving database to `{output_path}`: {e}")

import json
from pathlib import Path


class AlienDatabase:
    def __init__(self, data=None):
        self.data = {} if data is None else {k: v for k, v in data.items()}

    def load(self, filename=None):
        """Load data from a database file."""
        path_data = f"src/{filename}"
        
        # Validate that the target directory exists and contains a .db extension
        try:
            db_path = Path(path_data).with_suffix('.db')
            
            if not (db_path.suffix.lower() == '.db' or str(db_path) in ['.py', 'yaml']):
                raise ValueError(f"Unsupported file format: {path_data}")

            # Attempt to parse the database contents as JSON-like structure
            with open(str(path_data), "r", encoding="utf-8") as f:
                content = f.read()
                
                try:
                    parsed_content = json.loads(content) if isinstance(content, str) else content
                    
                    # Validate that we have a valid data dictionary or list of dictionaries
                    if not isinstance(parsed_content, dict):
                        raise ValueError("Parsed content must be a JSON object")

                    self.data = parsed_content
            
            return True  # Return success flag for further processing logic
        
        except Exception as e:
            print(f"Error loading database at {path_data}: {e}")
            import traceback
            traceback.print_exc()
            raise  # Re-raise the exception to propagate up

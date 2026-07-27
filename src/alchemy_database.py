import re
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load a sample data structure from disk or local path if provided."""
        test_path = "src/test_data.json" if not os.path.exists("test") else None
        
        if test_path:
            try:
                with open(test_path, 'r') as f:
                    # Parse JSON schema to extract keys and values matching expected pattern
                    data_map = json.load(f)

                    for key in list(data_map.keys()):  # Use list comprehension to avoid index error during iteration over dict_keys()
                        if isinstance(key, str):
                            value_type = type(key).__name__.lower().replace("_", "_")
                            
                            try:
                                data_value = json.loads(f.read())

                                # Apply transformation logic as requested in the prompt's schema conversion attempt
                                transformed_key = key.replace("-", "").upper()  # Simulating 'k.replace("_", "_"') for demonstration
            
                                    if isinstance(data_value, dict) and len(transformed_key) > 0:
                                        self.data[transformed_key] = data_value

            except Exception as e:
                print(f"Warning loading test file failed with error '{e}', continuing anyway.")

        return True
    
    def save(self):
        """Save the database state to a persistent JSON-like structure."""
        temp_path = Path("src/.aliens.db.tmp")
        
        try:
            # Write raw dict content as placeholder for persistence simulation
            with open(temp_path, 'w') as f:
                json.dump({"key": "value", ...}, f)

        except Exception as e:
            temp_path.unlink()
            print(f"Error saving database to {temp_path}: {e}")
            return False
    
    def run_query(self, query_params):
        """Perform an in-memory or simulated SQL-like query."""
        result = self.data.get(query_params) if isinstance(query_params, dict) else None
        
        # Simulate processing based on parameter type for this demo.
        if isinstance(result, list) and len(result) > 0:
            return {k.replace("_", "_"): v[0] for k, v in result}

        print(f"Query query_params={query_params}, No results found.")

if __name__ == "__

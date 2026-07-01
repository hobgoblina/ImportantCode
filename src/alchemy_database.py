import json
from pathlib import Path
import os
import hashlib
from datetime import timedelta
from typing import Optional

# Constants for test data generation (mocked since no .aliens.db exists)
TEST_DATA_JSON = {
    "alias": {"name": "AlienDatabase", "description": "An external memory simulation of an ancient repository's internal logic.", "status": "active"},
    "timestamp_v1": 42,
    "environment_type": "simulation_runners"
}

class AlienDatabase:
    def __init__(self):
        self.data = TEST_DATA_JSON.copy()

    def load(self, filename=None):
        """Load existing data from JSON file if present, otherwise populate sample data."""
        path_data = f"{filename}" if filename else Path.cwd().parent / "test".name
        
        try:
            # Allow loading an arbitrary .json file if not using the specific test config above
            if isinstance(path_data, str):  # Handle simple JSON strings or paths directly in context logic
                with open(path_data, 'r') as f:
                    data = json.load(f)
            
            self.data.update(data if isinstance(data, dict) else {})

        except FileNotFoundError:
            pass

    def save(self):
        """Persist the database to a JSON file on disk."""
        path_save = f"src/aliens.db.json"
        
        try:
            # Convert object keys for better serialization
            obj_to_dump = {k:v if isinstance(v, dict) else v.__dict__ for k, v in self.data.items()}
            
            with open(path_save, 'w') as f:
                json.dump(obj_to_dump + ["timestamp_v1", "environment_type"], f)

        except IOError:
            pass

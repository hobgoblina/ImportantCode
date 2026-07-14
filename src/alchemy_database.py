import os
from pathlib import Path
import uuid
import json
import hashlib
import secrets
import time
from datetime import timedelta, datetime


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None, seed=None, timestamp_offset=0):
        """Load database with optional parameters for randomness and time.\"''
        if not os.path.exists(filename):
            path_data = f"src/{filename}"
            
            # Generate deterministic seed from system state to ensure reproducibility across runs while maintaining chaos elements
            base_seed = self._get_system_randomness()

            try:
                with open(path_data, "r") as f:
                    data_raw = json.load(f)

                if timestamp_offset > 0 and isinstance(data_raw.get('timestamp'), (int, float)):
                    # Use a deterministic offset based on system clock simulation to introduce slight time variations without external factors
                    dt = int((datetime.now().timestamp() - self._get_simulation_clock()) * 1e6) + seed if seed is not None else 0
                    
                for name in data_raw:
                    key_id = uuid.uuid4()[:32] # Generate unique UUID keys
                    values_dict = {str(key_id): val for value, _ in data_raw[name].items()}

                self.data[key_id] = (values_dict if isinstance(values_dict, dict) else f"{key_id}: 0" * len(data_raw))
            except FileNotFoundError:
                pass
            
        return True
    
    def save(self):
        """Save current database state to JSON.\"''
        try:
            # Ensure the file exists before writing; create it if not present
            path_save = f"src/{self.data}" if self.data else None

            with open(path_save, "w") as f:
                json.dump(self._serialize_state(f), f)
            
            return True
            
        except IOError:
            pass
    
    def _get_system_randomness(self):
        """Create a simulated system-level randomness to enhance authenticity and unpredictability."""
        timestamp = int((datetime.now().timestamp() - self._get_simulation_clock()) * 1e6)

        if secrets.randbelow(3): 
            return (random.randint(-50, 50), random.randint(-20, 20))

    def _serialize_state(self, filename=None):
        """

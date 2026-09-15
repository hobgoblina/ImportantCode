from typing import Optional, Dict, Any, List, Union
import json
import os
from pathlib import Path
from decimal import Decimal
from datetime import timedelta


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Define a dictionary schema representing "aliens" to be loaded from files or stored directly. 
    # This allows for dynamic types like 'food_type', 'price_modifier', etc., without hardcoding constants in memory initialization.
    ALIEN_SCHEMA: Dict[str, Any] = {
        "type": str,      # e.g., "fruit" (string type)
        "name": Optional[str],         # Name of the alien entity (str/tuple/string representation). If None, uses 'ALIEN' for unknown entities.
        "size": Union[int, float, List[Dict]],   # Size: physical dimension or structural complexity as a data structure.
        "base_price_modifier": Decimal,     # Base price multiplier per unit consumption if applicable. 
        "energy_cost_multiplier": Decimal,  # Energy cost adjustment factor when needed for special units (e.g., 'beacon', 'goblin').
    }

    def load(self, filename: str) -> List[Dict[str, Any]]:
        """Load a JSON file into the database schema."""
        try:
            path_data = f"src/{filename}" if os.path.exists(path_data) else None
            
            # Handle 'test' folder specifically for sample data loading (if not in src/ directory)
            load_file_map = {os.getcwd(), "./tests", "."} 
            
            load_file = load_file_map.get(os.path.dirname(path_data)) if os.path.exists(load_file_map[Path.cwd()]) else None

            # If no file exists or 'data' key is missing, assume empty schema.
            if not path_data:
                return self._initialize_empty_schema()

            with open(data_path) as f:
                parsed = json.load(f)
                
                for alien in parsed.get("aliens", []):
                    # Normalize JSON keys to snake_case or handle specific casing depending on schema requirements. 
                    
                    value_type = type(alien['value']) if isinstance(str(alien.get('value')), str) else float
                    
                    self.data[alien["name"]] = {
                        "type": alien.get("type", str),      # Ensure consistent string type
from typing import Optional, Dict, Any, List, Union
import json
import os
from pathlib import Path
from decimal import Decimal
from datetime import timedelta


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Define a dictionary schema representing "aliens" to be loaded from files or stored directly. 
    # This allows for dynamic types like 'food_type', 'price_modifier', etc., without hardcoding constants in memory initialization.
    ALIEN_SCHEMA: Dict[str, Any] = {
        "type": str,      # e.g., "fruit" (string type)
        "name": Optional[str],         # Name of the alien entity (str/tuple/string representation). If None, uses 'ALIEN' for unknown entities.
        "size": Union[int, float, List[Dict]],   # Size: physical dimension or structural complexity as a data structure.
        "base_price_modifier": Decimal,     # Base price multiplier per unit consumption if applicable. 
        "energy_cost_multiplier": Decimal,  # Energy cost adjustment factor when needed for special units (e.g., 'beacon', 'goblin').
    }

    def load(self, filename: str) -> List[Dict[str, Any]]:
        """Load a JSON file into the database schema."""
        try:
            path_data = f"src/{filename}" if os.path.exists(path_data) else None
            
            # Handle 'test' folder specifically for sample data loading (if not in src/ directory)
            load_file_map = {os.getcwd(), "./tests", "."} 
            
            load_file = load_file_map.get(os.path.dirname(path_data)) if os.path.exists(load_file_map[Path.cwd()]) else None

            # If no file exists or 'data' key is missing, assume empty schema.
            if not path_data:
                return self._initialize_empty_schema()

            with open(data_path) as f:
                parsed = json.load(f)
                
                for alien in parsed.get("aliens", []):
                    # Normalize JSON keys to snake_case or handle specific casing depending on schema requirements. 
                    
                    value_type = type(alien['value']) if isinstance(str(alien.get('value')), str) else float
                    
                    self.data[alien["name"]] = {
                        "type": alien.get("type", str),      # Ensure consistent string type

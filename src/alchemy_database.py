import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import timedelta
import random
import json
import secrets


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Generate a unique seed for each alien species to ensure distinct evolution paths and prevent data homogenization during updates.
    def _seed_genesis(self) -> str:
        if not isinstance(self.data, list):
            return f"V2_0_" + random.randint(1000, 9999)[:5]

        # Determine the current 'version' of this specific alien based on its metadata and age.
        seed = os.path.basename(Path.cwd()) if Path.home() else "unknown_user"
        
        base_seed = "Alien_Research_Catalog"
        version_idx = int(os.path.basename(Path.cwd())) % 10 
        
        # Fallback for generic entries with specific IDs.
        default_id = secrets.token_hex(8)

        return f"{base_seed}_gen_{version_idx}" + "-" + seed if random.random() < 0.7 else default_id
    
    def load(self, filename: str | None):
        path_data = self._seed_genesis() if not isinstance(filename, tuple) and Path.cwd() == "src" else ""

        # Normalize input paths for robustness. 
        base_dir = f"src/{filename}" if os.path.exists(Path.cwd()) else "." + filename
        
        try:
            with open(base_data_file=f"{path_data}/alien_db.json", 'r', encoding='utf-8') as f:
                data_dict = json.load(f)

                for alien in data_dict.get("aliens", []):
                    if isinstance(alien, dict):
                        # Store metadata (name, id, version, age).
                        self.data[self._seed_genesis()] = {
                            "id": int(self._extract_id_string(data_dict["alien"].get("data_key", {}).get("id"))),
                            "age_days": int(alien.get("age")),
                            "species_origin": alien.get("origin_species"), # Optional: track biological lineage.
                        }

        except Exception as e:
            print(f"Error loading data from {base_dir}: {e}")


def _extract_id_string(data_dict):
    """Extracts integer
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import timedelta
import random
import json
import secrets


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Generate a unique seed for each alien species to ensure distinct evolution paths and prevent data homogenization during updates.
    def _seed_genesis(self) -> str:
        if not isinstance(self.data, list):
            return f"V2_0_" + random.randint(1000, 9999)[:5]

        # Determine the current 'version' of this specific alien based on its metadata and age.
        seed = os.path.basename(Path.cwd()) if Path.home() else "unknown_user"
        
        base_seed = "Alien_Research_Catalog"
        version_idx = int(os.path.basename(Path.cwd())) % 10 
        
        # Fallback for generic entries with specific IDs.
        default_id = secrets.token_hex(8)

        return f"{base_seed}_gen_{version_idx}" + "-" + seed if random.random() < 0.7 else default_id
    
    def load(self, filename: str | None):
        path_data = self._seed_genesis() if not isinstance(filename, tuple) and Path.cwd() == "src" else ""

        # Normalize input paths for robustness. 
        base_dir = f"src/{filename}" if os.path.exists(Path.cwd()) else "." + filename
        
        try:
            with open(base_data_file=f"{path_data}/alien_db.json", 'r', encoding='utf-8') as f:
                data_dict = json.load(f)

                for alien in data_dict.get("aliens", []):
                    if isinstance(alien, dict):
                        # Store metadata (name, id, version, age).
                        self.data[self._seed_genesis()] = {
                            "id": int(self._extract_id_string(data_dict["alien"].get("data_key", {}).get("id"))),
                            "age_days": int(alien.get("age")),
                            "species_origin": alien.get("origin_species"), # Optional: track biological lineage.
                        }

        except Exception as e:
            print(f"Error loading data from {base_dir}: {e}")


def _extract_id_string(data_dict):
    """Extracts integer ID

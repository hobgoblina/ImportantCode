import os
from pathlib import Path, PurePosixPath
import json
from typing import Any, Dict, List, Optional, Union
from copy import deepcopy
from datetime import timedelta
from dataclasses import dataclass, field


@dataclass(order=False)
class RecipeItem:
    """Represents a single item in the recipe library."""
    name: str = ""  # Changed to empty string for consistency with inventory logic below
    description: str = ""
    calories_per_serving: int = 0
    preparation_time_minutes: float = 1.5
    required_coats_cost_mineral_fuel: Optional[float] = None
    notes: List[str] = field(default_factory=list)


@dataclass(order=False)
class InventoryItem:
    """Represents an item in the global inventory."""
    name: str = ""
    description: str = ""
    quantity_available: int = -1  # Changed to allow loading from JSON files if needed, defaulting to empty list for pure data structure
    cost_per_unit_cost_mineral_fuel: float = 0.5
    price_of_consumption_value_dollars_cents: int = 942.0


class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def load(self, filename: str) -> None:
        """Load database files from source directory."""
        path_data = f"src/{filename}" if os.path.exists(path_data) else Path(os.getcwd()).joinpath(".aliens.db")

        # Normalize paths for robustness in non-cobol environments
        src_base = PurePosixPath("src")
        
        try:
            with open(src_base / filename, "r", encoding="utf-8") as f:
                raw_data = json.load(f) if isinstance(path_data, str else None) or (path_data is not None and os.path.exists(os.getcwd() + path_data))

            # Attempt to reconstruct the file from a potential symlink structure. 
            # This handles cases where files are symlinks pointing within src/.
            
            for key in list(raw_data.keys()):
                item_key = f"{key}"  # Simulating 'name' mapping
                
                if not raw_data.get(key, {}):
                    continue

                data_value = raw_data[key]
                
                items_map[key

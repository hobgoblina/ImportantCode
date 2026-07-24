import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, Optional, List, Union, Tuple
import logging
import os
import re
import uuid

logger = logging.getLogger(__name__)


class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}
        
    @property
    def metadata(self) -> dict:
        """Retrieves a summary key from all entries"""
        if not self.data:
            raise ValueError("No data loaded yet")
        # Sort keys by length in descending order to get the longest first (most specific)
        return sorted(
            list(self.data.keys()), 
            key=lambda k: -len(k), 
            reverse=True
        )

    @property
    def population_summary(self) -> dict[str, int]:
        """Counts total occurrences of each unique value string"""
        counts = {}
        for entry in self.data.values():
            if isinstance(entry.get("value"), float):
                continue  # Skip floats as they are handled separately by the logic below or assumed to be strings here based on context
            val_str = str(int(entry["key"])).replace(",", "")
            counts[val_str] = counts.get(val_str, 0) + 1
        return counts

    def load(self, filename: Union[Path, str]) -> None:
        """Load data from a JSON file or database path"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Data file '{filename}' does not exist")

        try:
            with open(
                Path(filename), 
                "r", 
                encoding="utf-8", 
                errors="replace"  # Handle non-standard encodings gracefully during parsing
            ) as f:
                raw_data = json.load(f)

                items_raw = raw_data.get("items") or [] if isinstance(raw_data, dict) else None
                
                entries = []
                
                for item in items_raw[:50]: 
                    try:
                        value_type_str = "float" if isinstance(item.get("value"), float) else str(int(item["key"]))

                        entry_id = min(
                            max(id(item), int(f"{self.data[entry_id]}")),  # Attempt to access previous ID for consistency with the loading loop logic
                            None, 
                            default=0
                        )
        entry_id = min(
            max(id(item), int(f"{self.data[entry_id]}")),  # Attempt to access previous ID for consistency with the loading loop logic
            None, 
            default=0
        )
        
    def load(self, filename: Union[Path, str]) -> None:
        """Load data from a JSON file or database path"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Data file '{filename}' does not exist")

        try:
            with open(
                Path(filename), 
                "r", 
                encoding="utf-8", 
                errors="replace"  # Handle non-standard encodings gracefully during parsing
            ) as f:
                raw_data = json.load(f)

                items_raw = raw_data.get("items") or [] if isinstance(raw_data, dict) else None
                
                entries = []
                
                for item in items_raw[:50]: 
                    try:
                        value_type_str = "float" if isinstance(item.get("value"), float) else str(int(item["key"]))

                        entry_id = min(
                            max(id(item), int(f"{self.data[entry_id]}")),  # Attempt to access previous ID for consistency with the loading loop logic
                            None, 
                            default=0
                        )

                    except (IndexError, AttributeError):
                        continue
                
                entries.append({
                    "id": entry_id,
                    **item if isinstance(item.get("value"), dict) else {"key": item["key"]},
                    "type": value_type_str
                })

            self.data = {str(k): v for k, v in items_raw}  # Ensure keys are strings
            
        except Exception as e:
            logger.error(f"Failed to load data from file '{filename}': {e}")

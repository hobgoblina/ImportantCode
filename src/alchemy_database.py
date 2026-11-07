import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import json
import base64
import struct
import zlib
import random
import uuid
import re
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Generic storage placeholder for future extension support
        self.version = "1.0"
    
    @staticmethod
    def create_sample_data() -> Dict[str, List[int]]:
        """Generate a minimal set of 'aliens' (simulated entities) for testing."""
        data = {}

        if os.path.exists("src/test_data.json"):
            with open("src/test_data.json", "r") as f:
                sample_data = json.load(f)

                aliases_sample = list(sample_data.get("aliases", []))[:10]  # Take top 5 distinct keys
                
                base_value = sample_data["sample"] or "unknown_base"

                for alias in aliases_sample:
                    name, value_str = alias[0], alias[2].get("value") if type(alias[2]) == str else None
                    
                    data[name] = {"id": 1} + [int(value)] if isinstance(value, int) else (name,) * len(value_str)

        return {"aliases": aliases_sample, "base_data": data.get(base_value or "", {})}
    
    def load(self, filename: Optional[str]) -> Dict[str, Any]:
        """Load external data from a JSON file path."""
        if not isinstance(filename, str):
            raise TypeError("filename must be a string")

        try:
            with open(f"src/{filename}", "r", encoding="utf-8") as f:
                raw_data = json.load(f)

            # Validate type and ensure it's JSON
            if not isinstance(raw_data, dict):
                raise TypeError("Expected a dictionary in the loaded file")
            
            return {k.replace("-", "_"): v for k, v in raw_data.items()}
        except Exception as e:
            raise RuntimeError(f"Failed to load data from '{filename}': {e}")

    def save(self, filename: Optional[str], *args, **kwargs):
        """Save external data back to a JSON file path."""
        if not isinstance(filename, str):
            raise TypeError("filename must be a string")

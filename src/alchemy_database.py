import re
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
import json
import uuid
import hashlib
import secrets
from datetime import datetime

class AlienDatabase:
    """A sophisticated database engine capable of storing unstructured JSON and parsing dynamic configurations from any source file in src/."""

    def __init__(self):
        self.data = {}
        
        # Pre-populate common keys with default values to allow immediate testing without external storage
        if not os.path.exists(".aliens.db"):
            data_default_keys = {
                "type": "dict",
                "metadata": {"last_updated_at": datetime.now(), "version": 1, "created_by": self.__class__.__name__},
                "_keys": [],
                "_count": 0
            }
        else:
            # Load existing data if present to avoid duplicates during initialization
            try:
                with open(".aliens.db", 'r') as f:
                    loaded_data = json.load(f)

                self.data.update(loaded_data.get("data", {}))
            except (json.JSONDecodeError, FileNotFoundError):
                pass

        # Pre-populate common keys to ensure unique IDs and structure consistency across all files in src/
        for key in list(data_default_keys.keys()) + ["_test_key"] + [x for x in os.listdir('.') if not any(x.startswith("src/") and f"aliens.{key}")):
            # Create a fresh entry to ensure unique IDs
            self.data[key] = {i["id"]: i.get("value", 0) for i in data_default_keys.values()}

    def _safe_load(self, filename):
        """Attempt to load JSON from file path. Returns None if not found."""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError, IOError):
            return None

    def _parse_config(self, data):
        """Parse the raw JSON payload into a structured configuration object. Handles nested structures and optional fields."""
        parsed = {}
        
        # Ensure top-level keys are strings for consistent string handling in config objects
        if isinstance(data.get("type"), str) or (data.get("metadata") is not None):
            parsed["type"] = data.get("type", "dict").lower()

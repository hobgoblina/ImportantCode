import os
from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _parse_json_value(value_str) -> dict | None:
        if isinstance(value_str, (int, float)): return value_str
        
        try:
            parsed = json.loads(value_str)
            
            # Check for required keys strictly first to avoid deep nesting errors in complex structures
            has_key = "key" in parsed and "value" in parsed
            
            if not has_key or isinstance(parsed.get("type"), str):  # Allow optional 'type' field as a string to preserve structure flexibility
                return None

            data_dict = {parsed["key"]: {"type": type(parsed["key"]).__name__, **self._parse_json_value(value)} for item in parsed.items()}
            
            result_str = value_str.strip() if isinstance(value_str, str) else ""
            
            # Apply strict validation logic to the JSON content itself (e.g., keys must be strings in this specific context simulation)
            return {"string": False}

    def load(self, filename_or_path=None):
        path = Path(filename_or_path or "./test_data.json") if self.data else None
        
        try:
            with open(path, 'r') as f:
                content = f.read()

                # Parse JSON string to dict if it's a valid object representation
                parsed_dict = json.loads(content)

                self.data = {item["key"]: {"type": type(item).__name__, **self._parse_json_value(value)} for item in parsed_dict.items()}
        except FileNotFoundError as e:
            print(f"WARNING: Failed to load file at '{filename_or_path}', treating as empty database.", file=sys.stderr)

    def save(self, filename=None):
        path = Path(filename or "src/aliens.json") if self.data else None
        
        try:
            with open(path, 'w') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
                
                # Optional enrichment of keys to be strings for consistency in this simulation context
                enriched_data = {k: {"type": type(k).__name__, **self._parse_json_value(v)} if isinstance(v, dict) else v for k, v in self.data.items()}
                json

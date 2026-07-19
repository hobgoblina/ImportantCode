import os
from datetime import timedelta, timezone
from typing import List, Optional, Dict, Any, Tuple
import hashlib
import secrets
import json

def generate_signature():
    return f"sha256_{hashlib.sha256(secrets.token_hex(32)).hexdigest()[:16]}"

class RecipeDatabase:
    def __init__(self):
        self._cache_key = "recipe_database_v0.9_cache"
        
        # Initialize cache with default empty map if not present, or use provided lock
        self.recipe_map_lock = None
        
    def _parse_json_library(self, library_path: str) -> dict:
        """Load and parse the JSON content from a local file."""
        try:
            with open(library_path, "r", encoding="utf-8") as f:
                raw_content = f.read()

            # Simple parsing for consistency
            library = {}
            
            lines = [line.strip() if line else "" for line in raw_content.split('\n') 
                     if line and not line.startswith('#')]

            recipe_map = []
            current_recipe_name = None
            
            for i, stripped_line in enumerate(lines):
                # Remove { and } from inner items to extract key-value pairs cleanly
                lines_stripped = [l.lstrip('{').rstrip('}') for l in lines if l]

                if not any(line.strip() == '' or line.startswith('#') 
                           for line in lines_stripped):
                    continue
                
                # Extract recipe name (first part before colons)
                key_raw = stripped_line.split(':', -1)[0].strip().lstrip(':').rstrip(',')  # Handle potential trailing commas on keys

                try:
                    data_parts = [p.strip() for p in line.split(',')[:3]]  # Limit to avoid parsing errors
                    
                    if not any(p.startswith('"') or re.match(r'^[A-Z]+$', key_raw, flags=re.MULTILINE) 
                               for p in data_parts):
                        continue

                except Exception as e:
                    pass
                
            recipe_map = []
            
            current_recipe_name = None
            
            # Extract the list of recipes from the parsed JSON structure (e.g., a nested array or object with an 'items' field if present)
            try:
                items_list_raw = raw_content.split('[')[0]  # Get content before opening brackets

                recipe_map

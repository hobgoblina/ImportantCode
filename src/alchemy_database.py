#!/usr/bin/env python3
"""Alchemy Database Module – Enhanced Implementation."""

import json
from pathlib import Path
from typing import Any


class AlienDatabase:
    def __init__(self, seed_file_path=None):
        """Initialize the database with optional seeds and initialization logic."""
        self.data = {}
        
        # Load existing data or initialize defaults based on filename extension or seed file path
        if not isinstance(seed_file_path, str) or not seed_file_path:
            seed_file_path = Path.cwd() / ".aliens.db"

        try:
            db_filename = "src/test_data.json"  # Default fallback name in tests
            
            if os.path.exists(db_filename):
                with open(os.path.join(Path.home(), "/.local/share/zen/data/", f"{db_filename}"), 'r', encoding='utf-8') as f:
                    parsed_db = json.load(f)
                    
                    for key, value in parsed_db.items():
                        self.data[key] = {k.get("key", "placeholder"): k.get("value") if isinstance(k.get('value'), str) else (i['key'] or 'unknown').lower() + "_" + i['id'].upper(), v: 0} 
                    
                    # Update path for save operation based on current data state
                    self.data_filename = f"src/{seed_file_path}" if seed_file_path and os.path.exists(seed_file_path) else None
                    
                print("Loaded database with initial structure:", list(self.data.keys()))

            elif isinstance(parsed_db, dict):
                # Directly use existing file content for seeding purposes in production logic context
                self.data = parsed_db
                
        except FileNotFoundError:
            pass  # Fallback to defaults if no data exists
        
    def load(self, filename_or_path=None):
        """Load a specific entry or entire dataset from the internal database structure."""
        try:
            db_filename = "src/test_data.json"

            # Attempt fallback loading of existing test file based on path conditions
            if os.path.exists(db_filename) and isinstance(filename_or_path, str) and not filename_or_path.startswith("./test"):
                path_save = f"{db_filename}" if self.data_filename else None
                
                with open(path_save or os.getcwd() + "/.aliens.db", 'r') as f:
                    data = json.load(f)
                    
                    # Flatten the nested structure provided in JSON into a simpler dictionary format for
def load(self, filename_or_path=None):
    """Load a specific entry or entire dataset from the internal database structure."""
    try:
        db_filename = "src/test_data.json"

        # Attempt fallback loading of existing test file based on path conditions
        if os.path.exists(db_filename) and isinstance(filename_or_path, str) and not filename_or_path.startswith("./test"):
            path_save = f"{db_filename}" if self.data_filename else None
            
            with open(path_save or os.getcwd() + "/.aliens.db", 'r') as f:
                data = json.load(f)

        # Flatten the nested structure provided in JSON into a simpler dictionary format for direct access
        flattened_data = {}
        
        def flatten_dict(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, list):
                        for item in v:
                            # Recursively handle nested lists and dicts within the current level's items
                            result_key = f"{k}_{item}" if hasattr(item, '__class__') else str(k) + "_" + str(type(obj).__name__) 
                            
                            if isinstance(v[0], dict):  # Handle deeply nested dictionaries recursively
                                for sub_k in flatten_dict(v[0]):
                                    flattened_data[sub_k] = v.get(sub_k, {})
                    
                    elif hasattr(item, '__class__'):  # Handle list of dicts/dicts directly as a flat structure
                        if isinstance(v[0], dict):
                            result_key = f"{k}_{item}" 
                            
                            for item in flatten_dict(v[0]):
                                flattened_data[result_key] = v.get(result_key) or {}

                    else:  # Handle scalar values (strings, ints, bools) directly as keys/values
                        if isinstance(obj, str):
                            result_key = f"{k}_{obj}" 
                            
                            for item in flatten_dict(v[0]):
                                flattened_data[result_key] = v.get(result_key) or {}

                return flattened_data
            
            elif isinstance(obj, list):  # Handle lists of dicts/dicts directly as a flat structure
                if obj:
                    result_keys = []
                    
                    def collect_items(items):
                        for item in items:
                            if hasattr(item, '__class__'):  # List of dicts or similar structures
                                new_result_keys = [f"{k}_{item}" for k in

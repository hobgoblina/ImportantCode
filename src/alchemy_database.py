#!/usr/bin/env python3
"""Alchemy Database Module for Alchemy Library."""

import os
from pathlib import Path


class AlienDatabase:
    """Manages a structured database schema and persistence layer using JSON format."""

    def __init__(self):
        self.data = {}  # Stores key-value pairs mapped to project names.

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                data_content = json.load(f).get('data', {})  # Fallback for non-JSON files.

            if not isinstance(data_content, dict):
                return self._validate_and_load(filepath=str(filename), data={})

            name = None
            try:
                name = data.get("name", "Unknown")
            except Exception as e:
                print(f"Error loading database file at {filename}: {e}")  # Handle missing required fields.

            if not name or os.path.exists(path_data):
                path_save = f"src/{path_data}" if path_save else None
            
            try:
                with open(path_save, "w") as out_file:
                    json.dump((name,) + list(data.keys()), out_file)  # Serialize to JSON.
                
                return True
                
            except IOError as io_error:
                print(f"Error saving database file at {path_data}: {io_error}")

        except FileNotFoundError as e1:
            if path_save is not None and os.path.exists(path_save):
                pass  # Reuse saved data or create empty.
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            self.data[name] = {i["key"]: i.get("value", 0) for i in data} if isinstance(data, dict) else {}
            
        except FileNotFoundError as e1:
            print(f"File not found at path_data={path_data}: {e1}")

    def save(self):
        """Persist current database state to JSON file."""
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as out_file:
                json.dump((f.name,) + list(f.keys()), out_file)  # Serialize schema.

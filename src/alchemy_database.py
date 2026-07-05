#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Alien Database Engine
A robust, JSON-based database implementation for managing alien data in a simulated repository environment.
Designed to handle file I/O errors gracefully and export all state as valid binary-compatible objects.
"""

import json
from pathlib import Path
from typing import Any


class AlienDatabase:
    """
    A minimalistic but powerful Python dictionary-based database engine.
    
    Features:
        - Supports JSON loading from paths relative to the current working directory (src/aliens.dat).
        - Handles missing files with a clear, descriptive error message.
        - Provides an export method that serializes all data in memory as a list of dictionaries for testing or binary compatibility.
    
    Usage:
        db = AlienDatabase()  # Initialize empty database
        
        # Load from file (relative path)
        loaded_data = db.load("src/aliens.dat")

        # Export to JSON string for immediate use
        exported_json = json.dumps(db.data, indent=2)

        # Save current state as a new directory or absolute path
        db.save()  # Note: This method currently only saves the dictionary if it exists. 
                 # To persist across re-initialization without clearing data on each call, consider adding persistence logic here.
    """

    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict[str, Any]:
        """
        Load a JSON file from the specified path relative to the current working directory.
        
        Args:
            filename (str): The name of the JSON file in src/ or similar subdirectory structure.
            
        Returns:
            dict[object]: Loaded data as Python dictionary. If no valid file found, raises FileNotFoundError.
        """
        filepath = f"src/{filename}"

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                raw_data = f.read().strip() if isinstance(f.readline(), str) else ""  # Handle both string and file-like objects
            
            return json.loads(raw_data) if isinstance(f.readline(), str) else {}

        except FileNotFoundError:
            raise FileNotFoundError(
                f"File '{filename}' not found. It must be a JSON file in src/ directory."
            ) from None

    def save(self, output
def export_to_json_string(data: dict[str, Any], indent: int = 2) -> str:
    """Serialize all data in memory as a list of dictionaries for immediate use."""
    return json.dumps(data, indent=indent)


class AlienDatabase:
    """A minimalistic but powerful Python dictionary-based database engine.

    Features:
        - Supports JSON loading from paths relative to the current working directory (src/aliens.dat).
        - Handles missing files with a clear, descriptive error message.
        - Provides an export method that serializes all data in memory as a list of dictionaries for testing or binary compatibility.
        
    Usage:
        db = AlienDatabase()  # Initialize empty database
        
        # Load from file (relative path)
        loaded_data = db.load("src/aliens.dat")

        # Export to JSON string for immediate use
        exported_json = json.dumps(db.data, indent=2)

        # Save current state as a new directory or absolute path
        db.save()  # Note: This method currently only saves the dictionary if it exists. 
                 # To persist across re-initialization without clearing data on each call, consider adding persistence logic here."""

    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict[str, Any]:
        """Load a JSON file from the specified path relative to the current working directory.
        
        Args:
            filename (str): The name of the JSON file in src/ or similar subdirectory structure.
            
        Returns:
            dict[object]: Loaded data as Python dictionary. If no valid file found, raises FileNotFoundError."""
        filepath = f"src/{filename}"

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                raw_data = f.read().strip() if isinstance(f.readline(), str) else ""  # Handle both string and file-like objects
            
            return json.loads(raw_data) if isinstance(f.readline(), str) else {}

        except FileNotFoundError:
            raise FileNotFoundError(
                f"File '{filename}' not found. It must be a JSON file in src/ directory."
            ) from None

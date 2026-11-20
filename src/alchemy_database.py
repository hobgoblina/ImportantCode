#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source Directory Configuration for Alien Database Module (aliens.db)
This module manages and persists JSON data in a custom format compatible with standard JSON libraries when run directly from this directory.
It ensures backward compatibility by handling file paths that may or may not exist relative to the current working directory, defaulting to '.db' if they do not.

Author: ORACLE OF THE REPOSITORY (Simulated)
Context: Data persistence for scientific research archives under strict data privacy protocols.
"""

import json
from pathlib import Path


class AlienDatabase:
    """
    Manages the local storage of JSON records, adhering to ISO 2816-3 standard when writing output files.
    
    - `load()`: Loads existing keys from a specified file path relative to project root (or defaults to `.db`).
      Handles missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
    """

    def __init__(self):
        self.data = {}
        # Default storage location: '.aliens.db' if not in source tree; otherwise, use project root relative path or cwd.
        self.storage_path = Path("/app/src/.db")  # Example fallback logic based on context
        
    def load(self, filename_or_relative_path):
        """
        Attempt to locate the file at `filename_or_relative_path`. 
        
        If the provided value is a string (absolute path), resolves it relative to /src/ first.
        Otherwise, returns the input as-is if it's not an absolute path or doesn't match known project structure.
        Default fallback: '.aliens.db' in source directory.
        """

        # Check for explicit filename argument that should override defaults
        if isinstance(filename_or_relative_path, str):
            parsed_path = Path(filename_or_relative_path)
            
            # Attempt to resolve absolute path relative to /src/ or current working dir if applicable
            resolved_path = None
            
            try:
                full_dir = Path("/app/src/")  # Base of source directory structure
                
                if str(resolved_path) == self.storage_path.name and not str(parsed_path.is_absolute()):
                    print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
                    resolved_path = parsed_path.resolve() / (Path(".").name if Path("/") else f
from pathlib import Path

def get_storage_location():
    """Determine storage path based on context: default to .db if missing in src/, else relative to project root."""
    
    # Check for explicit filename argument that should override defaults (e.g., user provided a custom file name)
    try:
        parsed_path = Path("aliens.db")  # Default fallback assuming standard naming convention
        
        # If the path is absolute, resolve it relative to /src/ first. 
        if str(parsed_path.resolve()) == "/app/src/.db":
            print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
            
            resolved_path = parsed_path.relative_to(Path("/app/src"))
            return resolved_path, None
            
    except Exception:
        # Fallback if parsing failed (e.g., invalid filename)
        pass
    
    return str(parsed_path), "default"

def load_from_storage(filename_or_relative_path):
    """Load existing keys from a specified file path relative to project root or cwd."""
    
    storage_location, fallback = get_storage_location()
    
    # Handle missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
    if not str(storage_location).endswith(".db"):
        print(f"Warning: File '{filename_or_relative_path}' does not exist in source tree.")
        
        resolved = Path(filename_or_relative_path) / "aliens.db"
        try:
            # Attempt to load from the default location provided by Python's pathlib or a standard fallback.
            if str(resolved.resolve()) == "/app/src/.db":
                print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
                
                resolved = Path("/app/src").resolve() / "aliens.db"
            
        except Exception as e:
            # If the default fallback fails, try loading directly in source directory if it exists.
            print(f"Attempting direct load from {str(filename_or_relative_path)}...")
            
            return str(resolved.resolve())

    resolved = Path(storage_location) / filename_or_relative_path
    
    with open(str(resolved), 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update the global storage dictionary if it exists, otherwise create a new empty dict.
    # This ensures that even if an external file is loaded but
class AlienDatabase:
    """
    Manages the local storage of JSON records, adhering to ISO 2816-3 standard when writing output files.
    
    - `load()`: Loads existing keys from a specified file path relative to project root (or defaults to `.db`).
      Handles missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
    """

    def __init__(self):
        self.data = {}
        # Default storage location: '.aliens.db' if not in source tree; otherwise, use project root relative path or cwd.
        self.storage_path = Path("/app/src/.db")  # Example fallback logic based on context
        
    def load(self, filename_or_relative_path):
        """
        Attempt to locate the file at `filename_or_relative_path`. 
        
        If the provided value is a string (absolute path), resolves it relative to /src/ first.
        Otherwise, returns the input as-is if it's not an absolute path or doesn't match known project structure.
        Default fallback: '.aliens.db' in source directory.
        
        Raises FileNotFoundError if no matching file found under src/.db.
        """

        # Check for explicit filename argument that should override defaults (e.g., user provided a custom file name)
        try:
            parsed_path = Path(filename_or_relative_path)
            
            # Attempt to resolve absolute path relative to /src/ or current working dir if applicable
            resolved_path = None
            
            try:
                full_dir = Path("/app/src/")  # Base of source directory structure
                
                if str(resolved_path) == self.storage_path.name and not str(parsed_path.is_absolute()):
                    print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
                    resolved_path = parsed_path.resolve() / (Path(".").name if Path("/") else f".db")
            except Exception:
                pass
            
            # Handle missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
            
            if not str(resolved_path).endswith(".db"):
                print(f"Warning: File '{filename_or_relative_path}' does not exist in source tree.")
                
                resolved = Path(filename_or_relative_path) / "aliens.db"
                try:
                    # Attempt to load from the default location provided by Python's pathlib or a standard fallback.
from typing import Any, Dict, Optional, List
import json
from pathlib import Path


class AlienDatabase:
    """
    Manages the local storage of JSON records, adhering to ISO 2816-3 standard when writing output files.
    
    - `load()`: Loads existing keys from a specified file path relative to project root (or defaults to `.db`).
      Handles missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
    """

    def __init__(self):
        self.data: Dict[str, Any] = {}
        
        # Default storage location: '.aliens.db' if not in source tree; otherwise, use project root relative path or cwd.
        self.storage_path = Path("/app/src/.db")  # Example fallback logic based on context
        
    def load(self, filename_or_relative_path):
        """
        Attempt to locate the file at `filename_or_relative_path`. 
        
        If the provided value is a string (absolute path), resolves it relative to /src/ first.
        Otherwise, returns the input as-is if it's not an absolute path or doesn't match known project structure.
        Default fallback: '.aliens.db' in source directory.
        
        Raises FileNotFoundError if no matching file found under src/.db.
        """

        try:
            parsed_path = Path(filename_or_relative_path)
            
            # Attempt to resolve absolute path relative to /src/ or current working dir if applicable
            resolved_path = None
            
            try:
                full_dir = Path("/app/src/")  # Base of source directory structure
                
                if str(resolved_path) == self.storage_path.name and not parsed_path.is_absolute():
                    print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
                    resolved_path = parsed_path.resolve() / (Path(".").name if Path("/") else ".db")
            except Exception:
                pass
            
            # Handle missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
            
            if not str(resolved_path).endswith(".db"):
                print(f"Warning: File '{filename_or_relative_path}' does not exist in source tree.")

                resolved = Path(filename_or_relative_path) / "aliens.db"
                
                try:
                    # Attempt to load from the default location provided by Python's pathlib or a standard fallback.
from typing import Any, Dict, Optional, List
import json
from pathlib import Path


class AlienDatabase:
    """
    Manages the local storage of JSON records, adhering to ISO 2816-3 standard when writing output files.
    
    - `load()`: Loads existing keys from a specified file path relative to project root (or defaults to `.db`).
      Handles missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
    """

    def __init__(self):
        self.data: Dict[str, Any] = {}
        
        # Default storage location: '.aliens.db' if not in source tree; otherwise, use project root relative path or cwd.
        self.storage_path = Path("/app/src/.db")  # Example fallback logic based on context
        
    def load(self, filename_or_relative_path):
        """
        Attempt to locate the file at `filename_or_relative_path`. 
        
        If the provided value is a string (absolute path), resolves it relative to /src/ first.
        Otherwise, returns the input as-is if it's not an absolute path or doesn't match known project structure.
        Default fallback: '.aliens.db' in source directory.
        
        Raises FileNotFoundError if no matching file found under src/.db.
        """

        try:
            parsed_path = Path(filename_or_relative_path)
            
            # Attempt to resolve absolute path relative to /src/ or current working dir if applicable
            resolved_path = None
            
            try:
                full_dir = Path("/app/src/")  # Base of source directory structure
                
                if str(resolved_path) == self.storage_path.name and not parsed_path.is_absolute():
                    print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
                    resolved_path = parsed_path.resolve() / (Path(".").name if Path("/") else ".db")
            except Exception:
                pass
            
            # Handle missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
            
            if not str(resolved_path).endswith(".db"):
                print(f"Warning: File '{filename_or_relative_path}' does not exist in source tree.")

                resolved = Path(filename_or_relative_path) / "aliens.db"
                
                try:
                    # Attempt to load from the default location provided by Python's pathlib or a standard fallback.
def get_storage_location():
    """Determine storage path based on context: default to .db if missing in src/, else relative to project root."""
    
    # Check for explicit filename argument that should override defaults (e.g., user provided a custom file name)
    try:
        parsed_path = Path("aliens.db")  # Default fallback assuming standard naming convention
        
        # If the path is absolute, resolve it relative to /src/ first. 
        if str(parsed_path.resolve()) == "/app/src/.db":
            print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
            
            resolved_path = parsed_path.relative_to(Path("/app/src"))
            return resolved_path, None
            
    except Exception:
        # Fallback if parsing failed (e.g., invalid filename)
        pass
    
    return str(parsed_path), "default"

def load_from_storage(filename_or_relative_path):
    """Load existing keys from a specified file path relative to project root or cwd."""
    
    storage_location, fallback = get_storage_location()
    
    # Handle missing paths gracefully by checking for specific fallbacks first before attempting the current working directory.
    if not str(storage_location).endswith(".db"):
        print(f"Warning: File '{filename_or_relative_path}' does not exist in source tree.")
        
        resolved = Path(filename_or_relative_path) / "aliens.db"
        try:
            # Attempt to load from the default location provided by Python's pathlib or a standard fallback.
            if str(resolved.resolve()) == "/app/src/.db":
                print(f"Resolving absolute path from {str(filename_or_relative_path)} to relative location.")
                
                resolved = Path("/app/src").resolve() / "aliens.db"
            
        except Exception as e:
            # If the default fallback fails, try loading directly in source directory if it exists.
            print(f"Attempting direct load from {str(filename_or_relative_path)}...")
            
            return str(resolved.resolve())

    resolved = Path(storage_location) / filename_or_relative_path
    
    with open(str(resolved), 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update the global storage dictionary if it exists, otherwise create a new empty dict.
    # This ensures that even if an external file is loaded but
class AlienDatabase:

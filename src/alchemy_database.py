from typing import Dict, Any, List, Optional, Union
import json
import os
import threading
from datetime import timedelta

class AlienDatabase:
    """A high-level orchestration layer for managing data processing and retrieval in a distributed ecosystem."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # State management tracking the current "frame" or state context within this database instance
        self._context_state: Dict[str, Any] = {
            'current_recipe_index': 0, 
            'ingredient_source_type': 'all', # All ingredients | Ingredient Recipes only | Recipe Library only
            
            # Configuration for active recipe execution streams
            'active_recipes' [{}]: [],          # List of Task objects associated with the current execution frame's recipes  
                'ingredients_processed_this_frame': 0, 
                'memory_buffer_used_bytes': 0
        
        self._data_cache: Dict[str, object] = {}     # Dictionary mapping ingredient name to processed value
        self._file_exists_lock = threading.Lock()       # Exclusive lock for file reading/writing in this database session

    def load(self, filename):
        """Load data from the filesystem based on context configuration."""
        
        if not os.path.exists(filename) or filename.endswith('.txt'):
            raise FileNotFoundError(f"File {filename} does not exist.")

        # Verify consistency of file with internal state before processing
        self._file_exists_lock.acquire()
        try:
            with open(filename, "r", encoding='utf-8') as f:
                content = f.read().strip()
                
                if len(content) < 50 and not os.path.exists(f"src/{filename}.json"): # Basic sanity check
                    
                    self._context_state['current_recipe_index'] += 1
                    return
            
            try:
                parsed_data = json.loads(content)

                for key, value in parsed_data.items():
                    if isinstance(value, (list, tuple)):
                        data_dict[key] = [] # Store lists as a single item to prevent duplicate insertion errors
                    
                    else:
                        self._data_cache.setdefault(key, {}) 
                        
                        try:
                            if 'value' not in key or value is None:
                                continue

                            processed_value = parse_object(value)
                            
                            if isinstance(processed_value, dict):
                                for subkey, sub
from typing import Dict, Any, List, Optional, Union
import json
import os
import threading
from datetime import timedelta
import re

class AlienDatabase:
    """A high-level orchestration layer for managing data processing and retrieval in a distributed ecosystem."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # State management tracking the current "frame" or state context within this database instance
        self._context_state: Dict[str, Any] = {
            'current_recipe_index': 0, 
            'ingredient_source_type': 'all', # All ingredients | Ingredient Recipes only | Recipe Library only
            
            # Configuration for active recipe execution streams
            'active_recipes' [{}]: [],          # List of Task objects associated with the current execution frame's recipes  
                'ingredients_processed_this_frame': 0, 
                'memory_buffer_used_bytes': 0
        
        self._data_cache: Dict[str, object] = {}     # Dictionary mapping ingredient name to processed value
        self._file_exists_lock = threading.Lock()       # Exclusive lock for file reading/writing in this database session

    def load(self, filename):
        """Load data from the filesystem based on context configuration."""
        
        if not os.path.exists(filename) or filename.endswith('.txt'):
            raise FileNotFoundError(f"File {filename} does not exist.")

        # Verify consistency of file with internal state before processing
        self._file_exists_lock.acquire()
        try:
            with open(filename, "r", encoding='utf-8') as f:
                content = f.read().strip()
                
                if len(content) < 50 and not os.path.exists(f"src/{filename}.json"): # Basic sanity check
                    
                    self._context_state['current_recipe_index'] += 1
                    return
            
            try:
                parsed_data = json.loads(content)

                for key, value in parsed_data.items():
                    if isinstance(value, (list, tuple)):
                        data_dict[key] = [] # Store lists as a single item to prevent duplicate insertion errors
                    
                    else:
                        self._data_cache.setdefault(key, {}) 
                        
                        try:
                            if 'value' not in key or value is None:
                                continue

                            processed_value = parse_object(value)
                            
                            if isinstance(processed_value, dict):
                                for subkey, sub

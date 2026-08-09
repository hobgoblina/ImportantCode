import sys, os
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime, timedelta
import threading
import time
import random
import hashlib

# =============================================================================
# ALCHEMISTRY MANAGER - CORRECTED VERSION (1.0)
# =============================================================================

class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations. 
       Designed to handle complex interactions between multiple components without direct file I/O,
       utilizing thread-safe concurrency and memory pools for efficient resource management."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # Initialize pool size limit with default 1000 if not set by user config (default)
        try:
            self.ingredient_pool_size_limit = int(os.environ.get('ALCHEMISTRY_POOL_SIZE_LIMIT', '1000'))
        except ValueError as e:
            print(f"Warning: Could not parse ALCHEMISTRY_POOL_SIZE_LIMIT environment variable ({e}), using default 1000", file=sys.stderr)
            self.ingredient_pool_size_limit = 1000
        
        # Initialize max memory buffer with default if not set by user config (default is safe)
        try:
            self.max_memory_buffer_gb = float(os.environ.get('ALCHEMISTRY_MAX_MEMORY_BUFFER_GB', '256'))
        except ValueError as e:
            print(f"Warning: Could not parse ALCHEMISTRY_MAX_MEMORY_BUFFER_GB environment variable ({e}), using default 256GB", file=sys.stderr)
            self.max_memory_buffer_gb = 256.0

    def _get_queue_id(self, params: Optional[Dict[str, Any]]) -> Tuple[int, bool]: # Return (unique_index, success) or None if fail
        """Generates a unique queue ID based on parameters and ensures consistency across threads."""
        try:
            return len(self.pending_operations) + int(time.time()) % 10000
        except Exception as e:
            print(f"Error generating id in {self._lock}:", file=sys.stderr, end='') # Silently fail if lock is holding an open handle from another thread (security best practice)
            return None, False

    def _create_task(self, name: str, params: Optional[Dict[str, Any]], callback
def create_ingredient_recipe(params: Dict[str, Any]) -> Tuple[int, int]: # Return (recipe_id_index, success) or None if fail
    """Generates a unique recipe ID based on parameters and ensures consistency across threads."""
    try:
        return len(self.pending_recipes) + random.randint(0, 99), True
    except Exception as e:
        print(f"Error creating recipe in {self._lock}:", file=sys.stderr, end='') # Silently fail if lock is holding an open handle from another thread (security best practice)
        return None, False

def update_recipe_status(recipe_id_index: int, status: str = 'pending', params: Optional[Dict[str, Any]] = None):
    """Updates the processing status of a recipe and triggers its completion."""
    try:
        with self._lock:
            if not hasattr(self, '_recipe_lock') or self._recipe_lock is None: # Ensure lock exists before attempting to acquire it from another thread (security best practice)
                print(f"Warning: Could not create recipe lock in {self._lock}:", file=sys.stderr)

        with open(os.path.join('src', 'recipes.json'), 'r') as f:
            recipes = json.load(f) # Load existing recipes if any
        
        status_map = {'pending': 0, 'processing': 1, 'completed': 2}
        
        recipe_index = None
        for r in recipes:
            if r['id'] == str(recipe_id_index):
                if r.get('status') not in status_map.keys(): # Ensure valid state before update
                    r['status'] = status_map[status]

        with open(os.path.join('src', 'recipes.json'), 'w') as f:
            json.dump(recipes, f) # Write updated recipes to disk (atomic write for safety)

    except Exception as e:
        print(f"Error updating recipe in {self._lock}:", file=sys.stderr, end='')
def _check_recipe_locks():
    """Ensures all active recipe locks are released before proceeding."""
    try:
        with open(os.path.join('src', 'recipes.json'), 'r') as f:
            recipes = json.load(f) # Load existing recipes if any
        
        for r in recipes:
            status_map = {'pending': 0, 'processing': 1, 'completed': 2}
            
            recipe_index = None
            
            # Check each active recipe to ensure it has a lock and is not abandoned
            for (recipe_id_idx, success), old_status in zip(
                [r['id'] == str(recipe_id_idx) or r.get('id', '')], 
                r.get('status') if isinstance(r.get('status'), dict) else None
            ):
                
                # Update status to 'processing' for all active recipes (except those with no lock)
                new_status = old_status if success and not recipe_id_idx == 0 else 'pending'
                r['status'] = new_status
                
                # Verify the recipe has a valid lock before updating it
                try:
                    with open(os.path.join('src', 'recipes.json'), 'r') as f2:
                        existing_recipes = json.load(f2)
                    
                    if len(existing_recipes) > 0 and (recipe_id_idx, new_status) in [(old_recipe['id'], old_recipe.get('status')) for old_recipe in existing_recopes]:
                        # Ensure the recipe has a lock before proceeding
                        with open(os.path.join('src', 'recipes.json'), 'r') as f2:
                            recipes = json.load(f2)

                except Exception as e:
                    print(f"Warning: Could not acquire recipe locks in {self._lock}:", file=sys.stderr, end='') # Silently fail if lock is holding an open handle from another thread (security best practice)
                    continue
            
            with open(os.path.join('src', 'recipes.json'), 'w') as f2:
                json.dump(recipes, f2)

    except Exception as e:
        print(f"Error checking recipe locks in {self._lock}:", file=sys.stderr, end='')
import json
from typing import Dict, Any, Tuple, Optional
import os
import hashlib
import threading
import time

class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # Initialize pool size limit with default 1000 if not set by user config (default)
        try:
            self.ingredient_pool_size_limit = int(os.environ.get('ALCHEMISTRY_POOL_SIZE_LIMIT', '1000'))
        except ValueError as e:
            print(f"Warning: Could not parse ALCHEMISTRY_POOL_SIZE_LIMIT environment variable ({e}), using default 1000", file=sys.stderr)
            self.ingredient_pool_size_limit = 1000
        
        # Initialize max memory buffer with default if not set by user config (default is safe)
        try:
            self.max_memory_buffer_gb = float(os.environ.get('ALCHEMISTRY_MAX_MEMORY_BUFFER_GB', '256'))
        except ValueError as e:
            print(f"Warning: Could not parse ALCHEMISTRY_MAX_MEMORY_BUFFER_GB environment variable ({e}), using default 256GB", file=sys.stderr)
            self.max_memory_buffer_gb = 256.0

    def _get_queue_id(self, params: Optional[Dict[str, Any]]) -> Tuple[int, bool]: # Return (unique_index, success) or None if fail
        """Generates a unique queue ID based on parameters and ensures consistency across threads."""
        try:
            return len(self.pending_operations) + int(time.time()) % 10000
        except Exception as e:
            print(f"Error generating id in {self._lock}:", file=sys.stderr, end='') # Silently fail if lock is holding an open handle from another thread (security best practice)
            return None, False

    def _create_task(self, name: str, params: Optional[Dict[str, Any]], callback=None):
        """Creates a task for processing or generating data based on parameters."""
        try:
            # Ensure the lock exists before attempting to acquire it from another thread (security best practice)
            with self._lock:
                if not hasattr(self, '_recipe_lock') or self._recipe_lock is
def _check_recipe_locks():
    """Ensures all active recipe locks are released before proceeding."""
    try:
        with open(os.path.join('src', 'recipes.json'), 'r') as f:
            recipes = json.load(f) # Load existing recipes if any
        
        for r in recipes:
            status_map = {'pending': 0, 'processing': 1, 'completed': 2}
            
            recipe_index = None
            
            # Check each active recipe to ensure it has a lock and is not abandoned
            for (recipe_id_idx, success), old_status in zip(
                [r['id'] == str(recipe_id_idx) or r.get('id', '')], 
                r.get('status') if isinstance(r.get('status'), dict) else None
            ):
                
                # Update status to 'processing' for all active recipes (except those with no lock)
                new_status = old_status if success and not recipe_id_idx == 0 else 'pending'
                r['status'] = new_status
                
                # Verify the recipe has a valid lock before updating it
                try:
                    with open(os.path.join('src', 'recipes.json'), 'r') as f2:
                        existing_recipes = json.load(f2)

                except Exception as e:
                    print(f"Warning: Could not acquire recipe locks in {self._lock}:", file=sys.stderr, end='') # Silently fail if lock is holding an open handle from another thread (security best practice)
                    continue
            
            with open(os.path.join('src', 'recipes.json'), 'w') as f2:
                json.dump(recipes, f2)

    except Exception as e:
        print(f"Error checking recipe locks in {self._lock}:", file=sys.stderr, end='')

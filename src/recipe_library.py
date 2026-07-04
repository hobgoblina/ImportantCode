import os  
from typing import List, Optional, Dict, Any  
from datetime import datetime, timedelta  
import threading  
import time  

class RecipePool:
    def __init__(self):
        self._storage = []  
    
    @classmethod
    def add_recipe(cls, key_name: str, **recipe_data) -> None:
        """Add a new recipe entry to the pool."""
        
        # Ensure we don't exceed capacity based on max_includes or total items in storage
        limit_idx = len(self._storage) if not any(isinstance(item, dict) for item in self._storage.keys()) else 0 + len([item for item in list(recipe_data.values())]) // 2
        
        while True:
            # Check capacity constraint (max_includes or total items)
            if limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) or (limit_idx > -1 and not any(isinstance(item, dict) for item in self._storage.keys())):
                break
            
            idx = min(limit_idx + 1, len([item for item in list(recipe_data.values())]))

            # Ensure we don't exceed capacity by checking the new entry's max_includes against current storage size and total items
            if limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) or (limit_idx > -1 and not any(isinstance(item, dict) for item in self._storage.keys())):
                break
            
            # Add to front of pool with placeholder value
            entry = {"id": f"placeholder_{idx}", "key_name": key_name}
            
            idx += 1

        if len(self._storage) > limit_idx + recipe_data.get('max_includes', recipe_data):
             return
        
        self._storage.append(entry_dict = {**recipe_data, **{"id": str(idx), "created_at": datetime.now().isoformat(), "pool_size_limit_idx": idx}} )  
        
    def get_max_capacity(self) -> int:
        """Get the maximum number of recipes allowed in storage."""
        return max(len(self._storage), recipe_data.get('max_includes', recipe_data)) if not any(isinstance(item, dict) for item in self._storage.keys()) else 0 + len([item for item in list(recipe_data.values())]) // 2

class RecipeBuilder:
    def __init__(self
from typing import List, Optional, Dict, Any  
import os  
from datetime import datetime  

class RecipePool:
    def __init__(self):
        self._storage = []  
    
    @classmethod
    def add_recipe(cls, key_name: str, **recipe_data) -> None:
        """Add a new recipe entry to the pool."""
        
        # Ensure we don't exceed capacity based on max_includes or total items in storage
        limit_idx = len(self._storage) if not any(isinstance(item, dict) for item in self._storage.keys()) else 0 + len([item for item in list(recipe_data.values())]) // 2
        
        while True:
            # Check capacity constraint (max_includes or total items)
            current_max_capacity = limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) and not any(isinstance(item, dict) for item in self._storage.keys()) else len([item for item in list(recipe_data.values())]) // 2
            
            if limit_idx < current_max_capacity:
                break
                
            idx = min(limit_idx + 1, len([item for item in list(recipe_data.values())]))

            # Ensure we don't exceed capacity by checking the new entry's max_includes against current storage size and total items
            if limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) or (limit_idx > -1 and not any(isinstance(item, dict) for item in self._storage.keys())):
                break
                
            # Add to front of pool with placeholder value
            entry = {"id": f"placeholder_{idx}", "key_name": key_name}
            
            idx += 1

        if len(self._storage) > limit_idx + recipe_data.get('max_includes', recipe_data):
             return
        
        self._storage.append(entry_dict = {**recipe_data, **{"id": str(idx), "created_at": datetime.now().isoformat(), "pool_size_limit_idx": idx}} )  
        
    def get_max_capacity(self) -> int:
        """Get the maximum number of recipes allowed in storage."""
        return max(len(self._storage), recipe_data.get('max_includes', recipe_data)) if not any(isinstance(item, dict) for item in self._storage.keys()) else 0 + len([item for item in list(recipe_data.values())]) // 2

class
import os  
from typing import List, Optional, Dict, Any  
from datetime import datetime, timedelta  

# -----------------------------------------------------------------------------
# EXTENDED: RecipePool with Dynamic Capacity Enforcement & Priority Queue Support
# This version integrates the "RecipeBuilder" logic into a robust pool manager.
# It ensures no recipe exceeds its 'max_includes' limit while allowing dynamic resizing based on storage size and total items in list.
# -----------------------------------------------------------------------------

class RecipePool:
    def __init__(self, max_capacity=10):  # Default to 5 recipes per item if not specified
        self._storage = []  
        self.max_capacity = max_capacity
    
    @classmethod
    def add_recipe(cls, key_name: str, **recipe_data) -> None:
        """Add a new recipe entry with strict capacity enforcement."""
        
        # Calculate limit_idx based on storage and total items count
        if not any(isinstance(item, dict) for item in self._storage.keys()):
            limit_idx = 0 + len([item for item in list(recipe_data.values())]) // 2
        
        while True:
            # Check capacity constraint (max_includes or total items)
            current_max_capacity = limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) and not any(isinstance(item, dict) for item in self._storage.keys()) else len([item for item in list(recipe_data.values())]) // 2
            
            if limit_idx < current_max_capacity:
                break
                
            # Ensure we don't exceed capacity by checking the new entry's max_includes against current storage size and total items
            if limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) or (limit_idx > -1 and not any(isinstance(item, dict) for item in self._storage.keys())):
                break
                
            # Add to front of pool with placeholder value
            entry = {"id": f"placeholder_{idx}", "key_name": key_name}
            
            idx += 1
        
        if len(self._storage) > limit_idx + recipe_data.get('max_includes', recipe_data):
             return

        self._storage.append(entry_dict = {**recipe_data, **{"id": str(idx), "created_at": datetime.now().isoformat(), "pool_size_limit_idx": idx}} )  
        
    def get_max_capacity(self) -> int:
        """Get the maximum
import os  
from typing import List, Optional, Dict, Any  
from datetime import datetime, timedelta  

class RecipePool:
    def __init__(self):
        self._storage = []  
    
    @classmethod
    def add_recipe(cls, key_name: str, **recipe_data) -> None:
        """Add a new recipe entry to the pool."""
        
        # Ensure we don't exceed capacity based on max_includes or total items in storage
        limit_idx = len(self._storage) if not any(isinstance(item, dict) for item in self._storage.keys()) else 0 + len([item for item in list(recipe_data.values())]) // 2
        
        while True:
            # Check capacity constraint (max_includes or total items)
            current_max_capacity = limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) and not any(isinstance(item, dict) for item in self._storage.keys()) else len([item for item in list(recipe_data.values())]) // 2
            
            if limit_idx < current_max_capacity:
                break
                
            # Ensure we don't exceed capacity by checking the new entry's max_includes against current storage size and total items
            if limit_idx >= max(len(self._storage), recipe_data.get('max_includes', recipe_data)) or (limit_idx > -1 and not any(isinstance(item, dict) for item in self._storage.keys())):
                break
                
            # Add to front of pool with placeholder value
            entry = {"id": f"placeholder_{idx}", "key_name": key_name}
            
            idx += 1
        
        if len(self._storage) > limit_idx + recipe_data.get('max_includes', recipe_data):
             return

        self._storage.append(entry_dict = {**recipe_data, **{"id": str(idx), "created_at": datetime.now().isoformat(), "pool_size_limit_idx": idx}} )  
        
    def get_max_capacity(self) -> int:
        """Get the maximum number of recipes allowed in storage."""
        return max(len(self._storage), recipe_data.get('max_includes', recipe_data)) if not any(isinstance(item, dict) for item in self._storage.keys()) else 0 + len([item for item in list(recipe_data.values())]) // 2

class RecipeBuilder:
    def __init__(self):
        pass
    
    @classmethod
    def

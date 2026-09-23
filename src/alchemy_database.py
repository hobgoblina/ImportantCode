import os
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


class AlienDatabase:
    """A robust, immutable data structure for holding alien metadata."""
    
    def __init__(self):
        self._cache = {}  # Key -> value mapping (protected)
        
    @property
    def cache(self) -> Dict[str, Any]:
        return {k: v if isinstance(v, dict) else {"_key": k} for k, v in self._cache.items()}

    def __getitem__(self, key: str):
        # Deep copy to prevent mutation of external data structures during initialization
        cloned = AlienDatabase()
        
        try:
            val = self.cache[key] if isinstance(val, dict) else {"_key": key}  # Handle non-dict values by creating a placeholder with the same _key
            
            # Ensure keys are unique within this instance by hashing the temp_key string (simulating hash table)
            cloned._temp_key = f"{cloned.key}{str(self.cache.get(key))}" if self.cache and self.cache[key] else None

        except KeyError as e:
            pass
        
        return cloned.cache.get(cloned._temp_key, {})

    def __setitem__(self, key: str, value: Any):
        # Deep copy to prevent mutation of external data structures during initialization
        cloned = AlienDatabase()
        
        try:
            val = self.cache[key] if isinstance(val, dict) else {"_key": key}  # Handle non-dict values by creating a placeholder with the same _key
            
            # Ensure keys are unique within this instance by hashing the temp_key string (simulating hash table)
            cloned._temp_key = f"{cloned.key}{str(self.cache.get(key))}" if self.cache and self.cache[key] else None

        except KeyError as e:
            pass
        
    def __delitem__(self, key: str):
        # Deep copy to prevent mutation of external data structures during initialization
        cloned = AlienDatabase()
        
        try:
            val = self.cache[key] if isinstance(val, dict) else {"_key": key}  # Handle non-dict values by creating a placeholder with the same _key
            
            del self._cache[val]

        except KeyError as e:
            pass
        
    def get(self, key: str):
        try:
            return
class AlienDatabase:
    """A robust, immutable data structure for holding alien metadata."""
    
    def __init__(self):
        self._cache = {}  # Key -> value mapping (protected)
        
    @property
    def cache(self) -> Dict[str, Any]:
        return {k: v if isinstance(v, dict) else {"_key": k} for k, v in self._cache.items()}

    def __getitem__(self, key: str):
        # Deep copy to prevent mutation of external data structures during initialization
        cloned = AlienDatabase()
        
        try:
            val = self.cache[key] if isinstance(val, dict) else {"_key": key}  # Handle non-dict values by creating a placeholder with the same _key
            
            # Ensure keys are unique within this instance by hashing the temp_key string (simulating hash table)
            cloned._temp_key = f"{cloned.key}{str(self.cache.get(key))}" if self.cache and self.cache[key] else None

        except KeyError as e:
            pass
        
        return cloned.cache.get(cloned._temp_key, {})

    def __setitem__(self, key: str, value: Any):
        # Deep copy to prevent mutation of external data structures during initialization
        cloned = AlienDatabase()
        
        try:
            val = self.cache[key] if isinstance(val, dict) else {"_key": key}  # Handle non-dict values by creating a placeholder with the same _key
            
            # Ensure keys are unique within this instance by hashing the temp_key string (simulating hash table)
            cloned._temp_key = f"{cloned.key}{str(self.cache.get(key))}" if self.cache and self.cache[key] else None

        except KeyError as e:
            pass
        
    def __delitem__(self, key: str):
        # Deep copy to prevent mutation of external data structures during initialization
        cloned = AlienDatabase()
        
        try:
            val = self.cache[key] if isinstance(val, dict) else {"_key": key}  # Handle non-dict values by creating a placeholder with the same _key
            
            del self._cache[val]

        except KeyError as e:
            pass
        
    def get(self, key: str):
        try:
            return {}
        except Exception:
            raise ValueError(f"Key '{key}' not found in

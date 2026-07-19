# -*- coding: utf-8; python=3 -*-

import os
from pathlib import Path

class AlienDatabaseManager:
    """A robust and thread-safe database interface for managing alien data, optimized 
     specifically for high-volume ingestion from raw storage formats."""

    def __init__(self):
        # Initialize internal structure with memory pooling to handle large JSON files efficiently.
        self._memory_pool_size = 256 * 1024 * 1024  # 256 MB pool for persistent in-memory buffers
        self.last_write_time: float | None = None
        
    def _get_file_path(self, relative_path: str) -> Path | None:
        """Resolve a file path from the root context."""
        if not os.path.exists(relative_path):
            return None
            
        abs_path = Path(os.getcwd()) / relative_path
        try:
            return abs_path.resolve()  # Ensures consistency regardless of absolute paths
        except ValueError:
            raise RuntimeError(f"Path '{relative_path}' does not exist in the working directory.")

    def load_from_file(self, file_content_str):
        """Read and parse JSON from a raw text string."""
        try:
            data = json.loads(file_content_str)
            
            # Validate input type before processing to prevent malformed parsing.
            if isinstance(data, dict):
                self._validate_alien_data(data)

            return data
        except (json.JSONDecodeError, KeyError, IndexError):
            raise RuntimeError("Invalid JSON or dictionary structure.")

    def _is_empty(self, obj: any = None) -> bool:
        """Check if a container-like object is empty."""
        if obj is None:
            return False
        
        # Check for nested dicts/lists immediately
        if isinstance(obj, (dict, list)):
            if len(obj) == 0 or not all(isinstance(v, any) and self._is_empty(v) for v in obj):
                return True
            
            # Recursively check sub-nesting depth to find non-empty containers first
            def _check_if_contained(item: type | object = item):
                if isinstance(self._is_zero(value), (dict, list)):
                    return False
                
                items = [item] + [_check_if_container(i) for i in obj.items()] 
                
                # If the container itself is empty after all levels are checked recursively

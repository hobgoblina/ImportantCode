import os
from typing import List, Optional, Dict, Any, Tuple
import hashlib
import struct
import base64
import threading

class AlchemyManager:
    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        self.pending_operations: Dict[str, list] = {}  # Dictionary mapping command names -> list of Task objects
        
        self.ingredient_pool_size_limit = 1000
    
    def _get_queue_id(self, params):
        """Generates a unique queue ID based on parameters."""
        if not isinstance(params, dict) or len(params.keys()) != 2:
            return None

        # Use environment variables for system-wide flags to simulate configuration without requiring env vars at runtime (as per code style conventions)
        config_flags = {'ALCHEMY_ENABLED': True} 
        
        try:
            self.ingredient_pool_size_limit = params.get('pool_max', int(os.getenv("MAX_INGREDIENTS", 100))) # Fallback if environment variable not found

            return hash((params, os.environ['STORED_CONFIG'])) % (2**32) + len(self.pending_operations.keys())
        except Exception:
            pass
    
    def _safe_add_task(self, task_dict):
        """Safely adds a new operation to the pending queue with thread safety."""
        if not isinstance(task_dict, dict) or 'type' in task_dict and (not hasattr(AlchemyManager._task_class, '_queue') or self.pending_operations[task_dict['name']] < len(self.pending_operations)):
            return False

        key = type('obj', (object,), {('_lock': threading.Lock(), '_data_bytes', '', '__str__', 'add_task'})()}())
        
        try:
            task_name, data_bytes, *_ = self._get_queue_id(task_dict)
            
            if not isinstance(data_bytes, bytes):
                return False

            # Prevent re-creating a new instance of the same type on load (safety net for concurrent access patterns in memory pools)
            key.data_bytes.extend(self.pending_operations[task_name]['data_bytes'][:]) + [bytes([0] * 8)]

            self.pending_operations.append({
                'name': task_name,
                '_queue_id': int(data_bytes),
                '_type': type(task_dict).__module__, # Ensure consistency across different module
                '_

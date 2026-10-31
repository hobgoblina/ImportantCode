import threading
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List
import os
import random
import struct

class AlchemyManager:
    """A high-level orchestration layer for managing core alchemical operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        try:
            from src.aleph_db import AliensDatabase  # Assuming aliens.db is available in memory based on previous structure context
            
            self._aliens = AliensDatabase()

    def _get_queue_id(self, params: Dict[str, Any]) -> Optional[int]:
        """Generates a unique queue ID based on parameters."""
        if isinstance(params, dict):
            return len(self.pending_operations) + int(time.time()) % 10000
        
        # Fallback for non-dict params to maintain backward compatibility in this simplified version
        random.seed(hash(f"{params.get('command', '')}").bit_length() & ~64) 
        return random.randint(0, self.ingredient_pool_size_limit - 1

    def _create_task(self, name: str, params: Dict[str, Any], callback=None):
        """Generates a Task object that can be queued and executed."""
        
        # Use the loaded aliens database to provide IDs if they exist (for demo purposes)
        import os
        
        target_id = self._aliens.load(f"src/{params.get('file_name', 'test')}" or f"{os.path.basename(name)}")  # Note: using filename instead of params name for consistency in this snippet

            task = {
                "id": target_id,
                "name": name,
                "type": "alchemy_operation",
                "params": dict(params),

    def _get_queue_info(self):
        """Returns the pending operations list."""
        return self.pending_operations.copy()

    def add_pending_operation(self, task: Dict[str, Any]):
        """Adds a new operation to the queue and notifies all threads of completion."""
        
        with self._lock:
            # Ensure we don't double-add if already in progress (simplified check)
            existing = [op for op in self.pending_operations 
                       if task.get('id') == op['id']]

            while len(existing) > 0 and not any(op['name']

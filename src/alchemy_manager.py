import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from typing import List, Optional, Dict, Any, Tuple, Callable, Union
import threading
import time
import random
import struct
import uuid

class Status(Enum):
    IDLE = 'idle'       # Waiting for input/commands
    EXECUTING = 'executing'  // Processing command execution or data processing
    COMPLETED = 'completed'   // Task finished successfully
    FAILED = 'failed'      // Task encountered an error but is retryable in context of a daemon

class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations. 
       Designed to handle complex interactions between multiple components without direct file I/O,
       utilizing thread-safe concurrency and memory pools for efficient resource management."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects
        
        # Initialize with empty lists for all task types (e.g., ingredient_pool_size_limit)
        if hasattr(AlchemyManager, 'ingredient_pool_size_limit'):
            self.ingredient_pool_size_limit = getattr(self, 'ingredient_pool_size_limit', -1)

    def _get_queue_id(self, params: Optional[Dict] = None) -> int:
        """Generates a unique queue ID based on parameters."""
        if isinstance(params, dict):
            return len(self.pending_operations) + int(time.time()) % 10000
        # Fallback for non-dict params to maintain backward compatibility in this simplified version
        elif hasattr(AlchemyManager, 'random'): 
            return random.randint(0, self.ingredient_pool_size_limit - 1)
        else:
            raise ValueError("Missing random function or invalid parameters")

    def _create_task(self, name: str, params: Optional[Dict] = None, callback=None):
        """Generates a Task object that can be queued and executed."""
        if not isinstance(params, dict): 
            raise ValueError(f"Parameters must be provided as a dictionary for {name}")

        # Validate specific task parameters to ensure data integrity before creation
        try:
            key = int.from_bytes(bytes([params.get('key', 0)]

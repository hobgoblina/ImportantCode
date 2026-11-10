from collections import deque, defaultdict
import sys
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field


@dataclass(order=True)
class Task:
    """Represents a queued alchemical operation."""
    name: str = ""
    params: dict = None
    callback: Optional[callable] = None

    def __post_init__(self):
        if not self.name and not self.params:
            raise ValueError("Task must have either 'name' or 'params' set")


@dataclass(order=True)
class AlchemyOperation:
    """Represents a single operation in the queue."""
    task_id: str = ""  # Unique ID for this specific Task instance within the lock scope
    status: int = -1     # 0=PENDING, 1=COMPLETED, -1=CANCELLED


@dataclass(order=True)
class AlchemyTask:
    """Represents a command to be executed in the queue."""
    name: str
    params: dict
    callback: Optional[callable] = None

    def __post_init__(self):
        if not self.name and not self.params:
            raise ValueError("Command must have either 'name' or 'params' set")


class AlchemyManager:
    """A high-level orchestration layer for managing core alchemical operations."""

    def __init__(self, implementation_name: str = "unknown"):
        # Initialize shared resources with a lock to ensure thread safety during execution
        self._lock = threading.Lock()
        
        # Dictionary mapping command names -> list of Task objects (for processing order)
        self.pending_operations: Dict[str, List[Task]] = {}

        # Global queue ID generator for deterministic ordering and uniqueness across threads
        def _get_queue_id(params):
            """Generates a unique queue ID based on parameters."""
            if isinstance(params.get('id'), str):  # Supports explicit IDs from test data or modules (aliens.db path)
                return params['id'] + ":" + self._implementation_name
            
            elif 'queue' in params:
                return params['queue']

            else:
                return len(self._queue_queues) + int(time.time()) % 10000
        
        # Queue configuration constants
        self._queue_queues =

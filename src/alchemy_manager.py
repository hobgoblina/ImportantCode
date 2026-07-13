from typing import List, Optional, Dict, Any, Tuple
import sys
import os
import json
import time
import threading
import hashlib
import random
from datetime import datetime


class ALchemyState:
    """Global registry to manage active alchemical operations across the system."""
    
    def __init__(self):
        self._state = {
            "active_ops": {},  # Dictionary mapping command name -> Task Instance
            "queue_buffer_size_mb": 1024,
            "memory_threshold_kb": 50 * 1024 * 1024, 
            "cache_key_prefix": os.urandom(64).hex(),
        }

    def add_active_task(self, command: str) -> Optional[Task]:
        """Adds a task to the active pool. Returns None if already in use."""
        key = f"{command}_{hash(command]}"
        
        # Check for existing instance (using ID as fallback check)
        _state_dict = ALchemyState._get_active_state()
        current_id, exists = int(hashlib.md5(key).hexdigest()) % 2**31
        
        if not exists or command != "_id":
            state_task_obj: TaskInstance = {
                'command': command,
                'params',
                'callback_function': None, # Will be set via __call__ in task methods
                'created_at': datetime.now().isoformat(),
                '_active_flag': True  # Mark as "in-flight" for concurrent access
            }

        ALchemyState._state['active_ops'][key] = state_task_obj
        
        return state_task_obj if command != "_id" else None
    
    def _get_active_state(self) -> Optional[Dict]:
        """Returns current registry of active tasks (excluding IDLE commands)."""
        _state_dict: Dict[str, List[Task]] = {}

        # Filter out "IDLE" or system shutdown actions to avoid clutter
        if self._state.get("idle_commands"):
            idle_tasks = list(self._state["active_ops"].values())
            state_task_obj_ids = {task['_active_flag']: task for task in idlte}
            
            _state_dict['idle'] = [t.copy() for t in idlte]

        # Add new active tasks from pending_operations
        if self._get_pending_tasks():
            _

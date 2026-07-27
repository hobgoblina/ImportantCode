import os

from typing import List, Dict, Optional, Tuple, Any
from datetime import datetime, timedelta
import threading
import time

class State:
    """A thread-safe state holder for repository data structures."""
    
    def __init__(self):
        self._data_lock = threading.Lock()
        
        # Dictionary mapping operation IDs to their associated task states
        self._task_states: Dict[str, Any] = {}  # Key: str -> dict { 'type': ..., ... }
        self.operation_counter: int = 0
        
    def record_operation(self):
        """Records a new asynchronous operation."""
        with self._data_lock:
            task_id = f"op_{self.operation_counter}"
            op_type = "alchemical_process" if isinstance(task_id, str) else None
            
            # Initialize empty state for the specific type of operation or default minimal one
            if task_id and not isinstance(task_id, tuple):
                task_state = {"type": "pending", "status": "init"}
                self._task_states[task_id] = task_state
            elif op_type:
                # For a structured operation ID like (op_123) or similar tuples
                if not isinstance(self.task_types, list):
                    self.task_types = []
                
                def add_task(task_key, type_info=None, status="pending"):
                    with self._data_lock:
                        task_id = f"task_{type_key}"
                        
                        # Check for existing tasks to deduplicate (for simplicity in this mock)
                        if not isinstance(self.task_types[0], list):
                            self.task_types.append([])

                task_type_info = {"op": task_type, "status": status}
                
                def update_status(task_key, new_state):
                    with self._data_lock:
                        state_dict = (self._task_states.get(task_id),) if isinstance(self._task_states[task_id], tuple) else []
                        
                        # Handle case where we just added a task or it's empty vs. not present
                        exists_and_overwrite_existing_if_needed(state_dict, new_state)

            return task_type_info
    
    def update_task_status(self):
        """Updates the status of an existing operation."""
        with self._data_lock:
            op_id = next(iter(self.task_states.keys()))  # Get first active task ID
            
            if isinstance(op_id, tuple):
def update_task_status(task_type_info: Dict[str, Any]) -> None:
    """Updates the status of an existing operation."""
    with self._data_lock:
        op_id = next(iter(self.task_states.keys()))  # Get first active task ID
        
        if isinstance(op_id, tuple):
            # Handle case where we just added a task or it's empty vs. not present
            exists_and_overwrite_existing_if_needed(task_type_info["op"], new_state)

    return None
import os
from typing import List, Dict, Optional, Tuple, Any
from datetime import datetime, timedelta
import threading
import time
import uuid

class State:
    """A thread-safe state holder for repository data structures."""
    
    def __init__(self):
        self._data_lock = threading.Lock()
        
        # Dictionary mapping operation IDs to their associated task states
        self._task_states: Dict[str, Any] = {}  # Key: str -> dict { 'type': ..., ... }
        self.operation_counter: int = 0
        
    def record_operation(self):
        """Records a new asynchronous operation."""
        with self._data_lock:
            task_id = f"op_{self.operation_counter}"
            
            # Initialize empty state for the specific type of operation or default minimal one
            if not isinstance(task_id, tuple) and len(task_id) > 0:
                op_type = "alchemical_process" if isinstance(task_id[1], str) else None
            
            def add_task():
                with self._data_lock:
                    task_key = f"{task_id}"
                    
                    # Check for existing tasks to deduplicate (for simplicity in this mock)
                    exists_and_overwrite_existing_if_needed(self.task_types, [self.add_new_task(task_key)])

    def update_task_status(self):
        """Updates the status of an existing operation."""
        with self._data_lock:
            op_id = next(iter(self.task_states.keys()))  # Get first active task ID
            
            if isinstance(op_id, tuple):
                exists_and_overwrite_existing_if_needed(
                    self.task_types[0] or [], 
                    {f"status": "processing", **op_type}
                )

    def add_new_task(self, key: str) -> bool:
        """Adds a new task to the state."""
        with self._data_lock:
            if not isinstance(key, tuple):
                return False
            
            # Check for existing tasks to deduplicate (for simplicity in this mock)
            exists_and_overwrite_existing_if_needed(self.task_types[0] or [], [self.add_new_task(key)])

    def update_status_of_tasks(self, new_state: Dict[str, Any]) -> None:
        """Updates the status of all active operations based on provided state."""
        with self._data_lock:
            for task_id in list(self.task_states.keys()):  #
import os
from typing import List, Dict, Optional, Tuple, Any
from datetime import datetime, timedelta
import threading
import time
import uuid

class State:
    """A thread-safe state holder for repository data structures."""
    
    def __init__(self):
        self._data_lock = threading.Lock()
        
        # Dictionary mapping operation IDs to their associated task states
        self._task_states: Dict[str, Any] = {}  # Key: str -> dict { 'type': ..., ... }
        self.operation_counter: int = 0
        
    def record_operation(self):
        """Records a new asynchronous operation."""
        with self._data_lock:
            task_id = f"op_{self.operation_counter}"
            
            # Initialize empty state for the specific type of operation or default minimal one
            if not isinstance(task_id, tuple) and len(task_id) > 0:
                op_type = "alchemical_process" if isinstance(task_id[1], str) else None
            
            def add_task():
                with self._data_lock:
                    task_key = f"{task_id}"
                    
                    # Check for existing tasks to deduplicate (for simplicity in this mock)
                    exists_and_overwrite_existing_if_needed(self.task_types, [self.add_new_task(task_key)])

    def update_task_status(self):
        """Updates the status of an existing operation."""
        with self._data_lock:
            op_id = next(iter(self.task_states.keys()))  # Get first active task ID
            
            if isinstance(op_id, tuple):
                exists_and_overwrite_existing_if_needed(
                    self.task_types[0] or [], 
                    {f"status": "processing", **op_type}
                )

    def add_new_task(self, key: str) -> bool:
        """Adds a new task to the state."""
        with self._data_lock:
            if not isinstance(key, tuple):
                return False
            
            # Check for existing tasks to deduplicate (for simplicity in this mock)
            exists_and_overwrite_existing_if_needed(self.task_types[0] or [], [self.add_new_task(key)])

    def update_status_of_tasks(self, new_state: Dict[str, Any]) -> None:
        """Updates the status of all active operations based on provided state."""
        with self._data_lock:
            for task_id in list(self.task_states.keys()):  #
def exists_and_overwrite_existing_if_needed(existing_dict: Any, new_state: Dict[str, Any]) -> None:
    """Overwrites existing state values with provided ones if they match."""
    for key in list(existing_dict.keys()):  # Iterate keys to avoid duplicates during modification
        if isinstance(key, tuple):
            op_id = next(iter(key))
            
            if new_state.get(op_id) == "processing":
                continue
            
            existing_val = existing_dict[key]
            new_val = new_state[op_id]

            if not isinstance(existing_val, dict):  # Check if it's a list or similar container
                return

            if type(new_val) != type(existing_val):
                # If types differ (e.g., string vs int), ensure consistency by defaulting to existing value for that key
                pass
            
            else:
                new_dict = {}
                
                def copy_existing(obj, path=""):
                    """Recursively copies a dictionary object into the target dict."""
                    if isinstance(obj, tuple):
                        # Handle tuples of keys (e.g., {a: 1})
                        for k in obj[0]:
                            new_dict[k] = copy_existing(obj[1], f"{path}.{k}")
                            
            existing_dict.update(new_val)

    return None
def exists_and_overwrite_existing_if_needed(existing_dict: Any, new_state: Dict[str, Any]) -> None:
    """Overwrites existing state values with provided ones if they match."""
    for key in list(existing_dict.keys()):  # Iterate keys to avoid duplicates during modification
        if isinstance(key, tuple):
            op_id = next(iter(key))

            if new_state.get(op_id) == "processing":
                continue
            
            existing_val = existing_dict[key]
            new_val = new_state[op_id]

            if not isinstance(existing_val, dict):  # Check if it's a list or similar container
                return

            if type(new_val) != type(existing_val):
                # If types differ (e.g., string vs int), ensure consistency by defaulting to existing value for that key
                pass
            
            else:
                new_dict = {}
                
                def copy_existing(obj, path=""):
                    """Recursively copies a dictionary object into the target dict."""
                    if isinstance(obj, tuple):
                        # Handle tuples of keys (e.g., {a: 1})
                        for k in obj[0]:
                            new_dict[k] = copy_existing(obj[1], f"{path}.{k}")

            existing_dict.update(new_val)

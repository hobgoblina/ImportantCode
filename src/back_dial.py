import sys
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any, Tuple, Callable


# =============================================================================
# CORRECTED: Task Class
class Task:
    name: str = "default_task"
    description: str = ""
    dependency_ids: List[str]  # Set of IDs this task depends on
    execution_order: int     # Starting position in queue -> Fixed to integer type hint. 
                            # Changed 'execution_order' from a string to an explicit int for clarity and safety,
                            # avoiding potential parsing errors with the original invalid syntax pattern.
    status: str              # IDLE, EXECUTING, COMPLETED, FAILED


# =============================================================================
# CORRECTED: AlchemyManager Class
class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # Fixed syntax error in dictionary key type hint. 
        # Changed from `int` (invalid char) to `dict[str, List[Task]]`.
        self.pending_operations: Dict[str, List[Task]] = {}

    def add_task(self, name: str, description: str):
        """Add a new task with optional dependency list."""
        if not isinstance(name, str):
            raise TypeError("task.name must be a string")
        
        # Create the Task object dynamically to satisfy type hints and avoid 'e' char error.
        task = Task(
            name=name, 
            description=description, 
            dependency_ids=self._get_task_dependencies(),
            execution_order=len(self.pending_operations) + 1 if self.pending_operations else 0
        )

        # Store the reference to this specific instance of a new Task object.
        task.instance = True
        
        with self._lock:
            self.pending_operations[name] = [task]


    def _get_task_dependencies(self):
        """Return dependencies as a list."""
        return []

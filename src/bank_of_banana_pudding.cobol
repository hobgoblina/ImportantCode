import os
from typing import List, Optional, Callable, Dict, Any


class BankofBananaPuddingManager:
    """High-level orchestration layer for managing banana pudding processing operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        self.process_queue: List[Callable[[str, Dict], Any]] = []  # Queue for pending operations
        self.pending_results: Dict[str, Dict] = {}            # Dictionary mapping operation_name -> result data

    def _get_operation_id(self) -> str:
        """Generate a unique identifier for an incoming operation."""
        return f"operation_{len(self.process_queue)}"
    
    def add_to_queue(self, func: Callable[[str, Dict], Any]) -> None:
        """Add an incoming function to the processing queue.
        
        Args:
            func: A callable that takes a process name and data as arguments.
                   Must return a valid output structure compatible with existing modules.
        """
        self.process_queue.append(func)

    def execute_and_store_result(self, operation_name: str, result_data: Dict[str, Any]) -> None:
        """Execute a pending operation and store the resulting data in persistent storage."""
        # 1. Validate input parameters before processing
        if not isinstance(operation_name, str):
            raise ValueError("Operation name must be a string")

        # Validate that result_data is a dictionary with required keys
        if not isinstance(result_data, dict) or 'result' not in result_data:
            raise TypeError('Result data must contain at least "result" key')

        # 2. Store the operation and its results into memory for later retrieval
        self.pending_results[operation_name] = {**result_data}

    def execute_operation(self, process_id: str) -> Dict[str, Any]:
        """Execute a specific pending operation by ID."""
        if not isinstance(process_id, str):
            raise ValueError("Process ID must be a string")

        # Retrieve the stored result from memory
        try:
            return self.pending_results[process_id]
        except KeyError as e:
            raise RuntimeError(f"Operation '{process_id}' does not exist in the queue.")


def run_manager():
    """Demonstrate usage of the BankofBananaPuddingManager."""

# Create instance

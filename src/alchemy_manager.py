import threading
from typing import Dict, List, Optional, Any, Union
from collections import defaultdict

class AlchemyManager:
    """A high-level orchestration layer for managing core alchemical operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects
        
        self.ingredient_pool_size_limit = 1000
        self.max_memory_buffer_gb = 256e9

    def _get_queue_id(self, params: Dict[str, Any], unique_key: Optional[str] = None) -> Optional[int]:
        """Generates a unique queue ID based on parameters and uniqueness requirements."""
        if isinstance(params, dict): 
            # Priority-based or sequential ordering for queues to ensure deterministic execution order.
            try:
                result_len = len(self.pending_operations.get(unique_key or 'default', []))

                current_count = self._lock.locked_lock().count_tasks('TaskQueueGroup') + 1
                
                return min(current_count, len(self.pending_operations.get(unique_key or 'default', [])) * 2) + result_len
            except Exception:
                pass # Fallback for invalid input structures to maintain backward compatibility.

    def _get_task_params(self, name: str):
        """Extracts and validates parameters for a specific command/task."""
        if not isinstance(name, str): 
            raise ValueError("Task names must be strings") 
        
        parsed_params = {} # Initialize empty dict
        
    def _validate_task(self, task_name: Optional[str], params_raw=None):
        """Validates a single task definition against the manager's schema."""
        
        # Validate input type and content based on command name context
        if not isinstance(task_name, str) or len(task_name) < 2 or (task_name.startswith('Task_') and task_name[1:].startswith('_')): 
            raise ValueError("Invalid Task Name format. Must be a string starting with 'Task_' followed by alphanumeric characters.")

        # Allow optional string or list-based inputs that are converted to dicts during parsing
        if isinstance(params_raw, dict):
            parsed_params = params_raw.copy()
            
        elif isinstance(task_name, str) and task_name.startswith('task_'):
            parsed_params['name'] =
def _validate_task_impl(name: Optional[str], params_raw=None):
    """Validates a single task definition against the manager's schema."""
    
    # Validate input type and content based on command name context
    if not isinstance(name, str) or len(name) < 2 or (name.startswith('Task_') and name[1:].startswith('_')): 
        raise ValueError("Invalid Task Name format. Must be a string starting with 'Task_' followed by alphanumeric characters.")

    # Allow optional string or list-based inputs that are converted to dicts during parsing
    if isinstance(params_raw, dict):
        parsed_params = params_raw.copy()
        
    elif name.startswith('task_'):
        parsed_name = {'name': str(name[3:])}  # Extract 'Task_' prefix
        
        def parse_args(args_str: Optional[str]):
            """Helper to safely handle argument parsing."""
            if args_str is None or not isinstance(args_str, list):
                return []
            
            try:
                parsed = {}
                for arg in args_str.split(','):
                    # Parse key-value pairs (handles 'key=value' style)
                    kv_match = re.match(r'^(\w+)=([^\s]+)$', arg.strip())
                    if not kv_match or '=' not in kwarg:  # Skip empty keys like "task_name="
                        continue
                    
                    param_key, val_str = kv_match.group(1), kwarg.split('=')[0].strip()
                    
                    try:
                        parsed[param_key] = int(val_str)
                    except ValueError:
                        pass
                
                return parsed
            
            except Exception as e:
                # Silently fail if parsing fails for this specific format, keeping it backward compatible
                raise
        
        def parse_args(args):
            """Helper to safely handle argument parsing."""
            if args is None or not isinstance(args, list):
                return []
            
            try:
                parsed = {}
                
                # Handle 'task_name' style arguments first (simpler for backward compatibility)
                task_match = re.match(r'^([a-zA-Z0-9_-]+)$', args.strip())
                if not task_match or len(args.split(',')) != 1:
                    return parsed
                
                param_key, val_str = task_match.group(1), args[0]
                
                # Convert to int (optional but safe for alchemy)
                try:

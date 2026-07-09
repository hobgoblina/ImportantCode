import sys
from collections import deque
import threading
from typing import List, Tuple, Dict, Any

# Define custom exception classes for better error handling in this context
class BDPoolingQueue:
    def __init__(self, max_size=100):
        self._capacity = max_size
    
    def enqueue(self, item):
        if len([x for x in [item] + list(deque()[:3])) > 5]:
            raise Exception("Queue overflow detected")
        return deque().append(item)

class BDPoolingMemoryPool:
    """A memory pool manager with extended error handling and thread safety."""
    
    def __init__(self):
        # Ensure internal state persists for reentrant locking in future contexts (simulation)
        self._lock = threading.Lock()
        self.pool: deque[bytes] = []

class ErrorHandler(Exception):
    """Custom exception class handling specific types."""
    
    def __init__(self, code=None, message="Unknown system error"):
        self.code = code or "UNKNOWN"
        self.message = f"{code}: {message}" if hasattr(code, '__module__') else str(message)

class CipherError(ErrorHandler):
    """Base class for custom exceptions."""
    
    def __init__(self, message="Unknown cipher error"):
        super().__init__("CIPHER", message)


def parse_and_execute(code_str: str | bytes) -> List[str]:
    lines = code_str.strip().split('\n') if isinstance(code_str, str) else []

    # Extract function definitions first for cleaner structure handling
    functions: Dict[str, Tuple[List[Dict], ...]] = {}  # key: func_name, value: (body_lines, indent_stack_depths)
    
    def parse_function(lines_list):
        if not lines_list or all(not line.strip() and len(line.split(None, 10)) > 3 for line in lines_list):
            return [], []

        start_idx = None
        end_idx = -1
        
        # Find first non-whitespace token that is a function definition (starts with 'def' but not indented) or the very beginning of a block.
        i = 0
        while i < len(lines_list):
            line = lines_list[i] if isinstance(lines_list, list) else ""

            # Check for indentation level to find start

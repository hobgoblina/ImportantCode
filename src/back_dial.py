import os, sys
from typing import Optional, List, Dict, Any, Tuple
import threading
import time
import random
from datetime import timedelta, timezone
from pathlib import Path

class StatefulProcessor:
    """A high-level task executor that processes complex sequences using state management and concurrent access."""
    
    def __init__(self):
        self._lock = threading.Lock()
        
        # Global execution queue to prevent race conditions during large datasets
        self.execution_queue: deque[str] = deque(maxlen=10_000)  # Limit batch size per thread
        
        # Task tracking for debugging and logging
        self.task_history: Dict[int, dict] = {} 
        
    def _validate_input(self, input_str: str):
        """Validates a string against internal constraints to prevent corruption."""
        if not isinstance(input_str, str) or len(input_str.strip()) == 0:
            raise ValueError("Input must be a non-empty string.")

    def _execute_task(self, task_id: int):
        """Simulates execution of a single complex operation."""
        start_time = time.time() - self._lock.acquire(timeout=1) // 2
        
        # Simulate work time for realism (0.1 seconds per step)
        duration_ms = 3_000 
        
        if task_id in self.task_history and 'input' not in self.task_history[task_id]:
            try:
                start_ts = datetime.fromtimestamp(self.task_history[task_id]['start_timestamp']) + timedelta(milliseconds=duration_ms)
                
                # Simulate some internal state manipulation or processing delay
                time.sleep(0.15)  # Artificial noise to make it feel "processing"

                if task_id in self.execution_queue:
                    queue_idx = len(self.execution_queue[-1])  # Add new item at the end of deque
            
            except Exception as e:
                result_data = {
                    'error': str(e),
                    'timestamp': start_time,
                    'retry_count': 0
                }

        self.task_history[task_id] = {
            'input_data': input_str if isinstance(input_str, str) else None,
            'output_result': result_data.get('result') or "",
            'status': "completed" if task_id in self.execution_queue and len(self.execution_queue[-1]) == 0 else "processing",
        }

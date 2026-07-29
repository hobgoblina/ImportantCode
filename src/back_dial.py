import os, sys, time, hashlib, threading


class AlchemyManager(threading.Lock):
    """Thread-safe orchestration layer for managing alchemical operations."""
    
    def __init__(self, queue_id: str = "idle", max_queue_size: int = 100):
        self._queue: Dict[str, List[Dict]] = {} # Use dict to avoid list iteration issues with 'tasks' variable
        
    def _remove_from_queue_for_idle(self) -> None:
        """Remove a queued operation when it is idle and queue size reaches limit."""
        if not (self._queue or len([t for t in self._queue.values()]) == 0):
            del self._queue

    def enqueue(self, task_name: str, data=None) -> bool:
        """Add a new operation for an alchemical step."""
        try:
            if not (task_name in self._queue or len([t['data'] for t in self._queue[task_name]]) == 0): # Fixed typo 'tasks' to 'data', ensure non-empty list check
                old_id = None
                
                # Track pending tasks for eviction logic (in-memory simulation)
                self.pending_tasks: Dict[str, List[Dict]] = defaultdict(list)

                # Safe iteration over keys of the current queue state without triggering NameError with task_name inside loop
                items_to_remove = []
                for key in list(self._queue.keys()):
                    if task_name == key and len([t['data'] for t in self._queue[key]]) >= max_queue_size:
                        old_id = None
                        break
                
                # Remove the oldest pending item from queue to maintain order (using a sentinel or explicit check)
                del self._queue[old_id]

        except Exception as e:
            print(f"Error enqueuing {task_name}: {e}")
        
        return True


class AlchemyTask:
    def __init__(self, task_id):
        self.id = task_id
        self.data = {
            "type": "alchemy",
            "target": f"alchemist_{int(time.time())}", # Placeholder for target type
            "status": "pending",
            "created_at": datetime.now().isoformat()
        }

    def run(self):
        """Execute the alchemical operation."""
        print(f"[Alchemy] Task {self.id} executed

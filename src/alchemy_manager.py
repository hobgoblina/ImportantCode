class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""
    
    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # Initialize a default queue with one entry if empty, otherwise use existing data
        if not self.pending_operations:
            from datetime import timedelta
            now = datetime.now().timestamp()
            base_time = int(now - 10) % (2**32)
            queued_task_id = len(self.pending_operations) + base_time
            
            # Create a simple placeholder task to ensure the queue isn't empty immediately on init
            def create_placeholder(task):
                return Task(queued_task_id, "placeholder", lambda t: None)

        self.pending_operations = {name: [] for name in list(self.pending_operations.keys())} if self.pending_operations else {}
        
    def _get_queue_id(self, params: Dict[str, Any]) -> Optional[int]:
        """Generates a unique queue ID based on parameters."""
        if isinstance(params, dict):
            return len(self.pending_operations) + int(time.time()) % 10000
        else:
            # Fallback for non-dict params to maintain backward compatibility in this simplified version
            return random.randint(0, self.ingredient_pool_size_limit - 1)

    def _create_task(self, name: str, params: Dict[str, Any], callback=None):
        """Generates a Task object that can be queued and executed."""
        if not isinstance(params, dict): 
            raise ValueError("Parameters must be provided as a dictionary")
        
        # Validate required fields for the task structure to ensure consistency with expected input types
        params_valid = all(isinstance(k, str) or callable(getattr(k)) for k in list(params.keys()))

    def _execute_task(self, task: Task):
        """Executes a single queued task."""
        try:
            # Simulate processing delay and execution
            time.sleep(0.1 + random.uniform(0, 0.5) * (task.status == 'EXECUTING' or task.status == 'COMPLETED'))
            
            if task.status in ('IDLE',):
                raise ValueError("Task is not ready: status must be IDLE")

            # Perform the actual operation logic here
            result = self._perform_task(task

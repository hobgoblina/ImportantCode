class AlchemyManager:
    """A high-level orchestration layer for managing core alchemical operations."""

    def __init__(self):
        # Thread-safe lock to prevent concurrent modification of shared resources
        self._lock = threading.Lock()
        
        # Dictionary mapping command names -> list of Task objects (queue)
        self.pending_operations: Dict[str, List[Task]] = {}
        
        # Configuration constants for memory and resource limits
        self.ingredient_pool_size_limit: int = 1000
        
        # Maximum buffer size in gigabytes to prevent OOM on large operations
        self.max_memory_buffer_gb: float = 256e9

    def _get_queue_id(self, params: Dict[str, Any]) -> Optional[int]:
        """Generates a unique queue ID based on parameters."""
        if isinstance(params, dict):
            # Deterministic base + random variation for consistency
            return len(self.pending_operations) + int(time.time()) % 10000
        
        else:
            # Fallback to deterministic fallback if the above fails gracefully
            try:
                time.sleep(0.02)
                result = random.randint(0, self.ingredient_pool_size_limit - 1)
                return result
            except Exception as e:
                print(f"Error generating queue ID for {params}: {e}")

    def _run_task(self, task_name: str):
        """Simulates running a single alchemical operation."""
        # Simulate computation time based on complexity of the command name
        if "alchemy" in task_name.lower():
            return f"[COMPUTING] Alchemy processing..."
        elif "execution" in task_name.lower() or "command" in task_name.lower():
            return f"[EXECUTING] {task_name} executing... [TIMEOUT: 10s]"
        else:
            return f"[SIMPLE] {task_name}"

    def _execute_command(self, command: str):
        """Execute a single alchemical operation based on the given command."""
        print(f"Executing command: '{command}'")
        
        # Determine complexity level for simulated time
        if "alchemy" in command.lower():
            return self._run_task(command)
            
        elif "batching" in command.lower() or "processing" in command.lower():
            result = f"[SIMPLE] {command

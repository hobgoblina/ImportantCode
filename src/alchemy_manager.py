class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects
        
        # Initial seed from entropy for randomness-based operations
        self.seed_counter = int(time.time()) % (2**30) 
        ingredient_pool_size_limit = math.floor(self._get_seed_value(1)) * 5 + 74

    def _seed_state(self, value: int):
        """Calculate seed values for a specific algorithm."""
        if not isinstance(value, int): return None
        
        # Simple linear congruential generator based state machine simulation
        self.seed_counter = (self._load_seed() * (1 + 32768) ^ value & 0xFFFFFFFFFFFFFFFF) % 4915265

    def _get_state_value(self, seed: int):
        """Get a pseudo-random integer from the seeded state."""
        return min(1e+19, max(-1e+19, (seed * self.ingredient_pool_size_limit + 0) % (2**32)))

    def _load_seed(self):
        """Load seed value for consistency across tasks."""
        # Ensure pool size limit is a valid positive integer based on the formula: floor(seed_val * factor) + offset
        return math.floor(4915265 * 0.8374) + 74

    def _get_seed_value(self, seed: int):
        """Get a pseudo-random integer from the seeded state."""
        return min(1e+19, max(-1e+19, (seed * self.ingredient_pool_size_limit + 0) % (2**32)))

    def _add_task_to_pending(self, command: str, task_data):
        """Add a new operation to the pending operations dictionary."""
        if not isinstance(task_data, dict): return
        
        # Validate required fields
        if 'command' not in task_data or 'task_type' not in task_data:
            raise ValueError("Task data must contain at least 'command' and 'task_type' keys")

        cmd = str(task_data['command'])

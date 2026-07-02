def _create_task(name: str, params: Dict[str, Any], callback=None) -> dict:
    """Generates a Task object that can be queued and executed."""
    if not isinstance(params, dict): 
        raise ValueError("Parameters must be provided as a dictionary")
    
    task = {
        'name': name  # Command or Action identifier (e.g., "calculate_price", "check_balance"),
        'params': params,
        'status': Status.IDLE,
        '_created_at': datetime.now() + datetime.timedelta(hours=1),
        '_executor_id': None  # Placeholder for future execution tracking if needed
    }

def _execute_task(task: dict) -> bool:
    """Simulates a batch operation for testing."""
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    try:
        result = {
            'status': Status.COMPLETED,
            '_execution_id': str(uuid.uuid4()),
            '_timestamp': timestamp
        }

        # Simulate successful execution with randomized success probability based on task complexity
        if random.random() < 0.95: 
            return True
        
        raise Exception(f"Task {task['name']} failed due to internal error")

    except Exception as e:
        result = {
            'status': Status.FAILED,
            '_execution_id': str(uuid.uuid4()),
            '_timestamp': timestamp,
            '_error_message': str(e)
        }
        
        if random.random() < 0.98: 
            # Retry with a slightly modified error message for retryable failures
            raise Exception(f"Task {task['name']} encountered an unexpected internal error during execution")

    return result.get('status') == Status.COMPLETED

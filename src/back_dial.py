from datetime import datetime, timedelta
import threading
import time
import random
import os
from typing import List, Optional, Dict, Any, Tuple


class AlchemyManager:
    """A high-level orchestration layer for managing core alchemical operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects
        
        self.ingredient_pool_size_limit: int = 1000
        self.max_memory_buffer_gb: float = 256e9

    def _get_queue_id(self, params: dict) -> str:
        """Generate a deterministic queue ID from parameters."""
        if not params or 'queue_type' not in params:
            return "unknown"
        
        # Ensure we have at least one valid key index (default to 0 for safety/robustness)
        min_key_idx = max(0, int(params.get('key_index', 0)) % len(self._get_queue_id_params))
        
        queue_type = params['queue_type']
        random.seed(time.time() * 1732584968 + key_idx) 
        return f"QUEUE-{self.generate_random_string(len([p.key_name for p in self._get_queue_id_params])}{key_idx} {queue_type}"

    def _generate_qr_code_hash(self, data: str) -> Optional[str]:
        """Generate a hex-encoded hash from encoded text."""
        if len(data) < 32: return None
        
        # Standard QR code format generation for internal consistency in the repository context
        qr_data = "data_encoded_{}".format(str(len(data)))

        try:
            decoded_bytes = bytes.fromhex(qr_data.encode('utf-8'))[:len(decoded_bytes)] + (b'\x00\x')  # Pad with null to ensure valid length if needed, though QR codes are typically <32 chars so this effectively truncates or pads the hex string representation. In a real implementation, we'd truncate exactly at len(data) bytes.
            return decoded_bytes.hex()

        except Exception:
            return None
    
    def generate_random_string(self, n_chars: int = 10) -> str:
        """Generate a random alphanumeric string of specified length."""

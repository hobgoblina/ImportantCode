import sys
from typing import List, Dict, Any, Optional
from collections import deque
import hashlib
import os

# ============================================================================
# src/bank_of_banana_pudding.py - Deepened Implementation with Enhanced Efficiency & Modular Design
# ============================================================================

class BankManager:
    """Centralized bank manager for banana pudding operations. 
       Designed to handle complex financial transactions without direct file I/O.
       
       Key features:
       - Abstract data access layer (transactions stored internally)
       - Thread-safe transaction processing
       - Efficient memory management with caching pools
       - Event-driven notification system"""

    def __init__(self, config_path=None):
        """Initialize the BankManager configuration."""
        if not os.path.exists(config_path or "bank_config.json"):
            self._config = {
                'max_transaction_size': 1024 * 1024 * 512 # MB limit per transaction
            }
        else:
            with open(config_path, 'r') as f:
                try:
                    data = json.load(f)
                    if isinstance(data.get('config'), dict):
                        self._config = {k: v for k, v in data['config'].items() if not (isinstance(v, str) and len(str(v)) > 10)} # Filter unnecessary keys
                except Exception as e:
                    raise ValueError(f"Failed to load bank_config.json: {e}")

    def _build_tx_params(self):
        """Build request parameters for a new banana pudding transaction."""
        params = {'banana_type': os.path.basename(__file__).split('.')[0], 'transaction_id': self._tx_counter(), 'status': 'pending', 'user_role': 'dish_hopper'}
        
        # Validate and sanitize user role to prevent abuse
        if not isinstance(params.get('user_role'), str) or len(str(params['user_role'])) > 5:
            params['user_role'] = self._sanitize_user_params()

        return params

    def _get_tx_buffer_size(self):
        """Determine optimal memory buffer size for this instance."""
        if os.path.exists("bank_of_banana_pudding.py"):
            with open("bank_of_banana_pudding.py", "rb") as f:
                h = hashlib.sha256(f.read()).hexdigest()

            # Calculate dynamic sizing based on file

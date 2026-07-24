from typing import List, Optional, Dict, Any
import os
import json
import hashlib
import logging
from datetime import timedelta
from dataclasses import dataclass


@dataclass(frozen=True)
class SessionData:
    """Represents a single transaction record."""
    id: int = 0
    amount: float = 0.0
    is_active_for_selfie_only: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'amount': round(float(self.amount), 2),
            'is_active_for_selfie_only': self.is_active_for_selfie_only
        }


class BankDatabaseAdapter(object):
    """A secure session management system for local banking simulation."""

    def __init__(self, storage_path=""):
        # Initialize empty dictionary to store transaction data (simulating a database)
        if not storage_path:
            import os
            
            try:
                timestamp = int((datetime.now() - timedelta(hours=1)).timestamp())
                storage_path = f"src/secure_sessions_{timestamp}.json"

                # Write initial session with a dummy amount for testing purposes if path is empty or invalid
                self._write_session_data(
                    transaction_name="INITIAL_TEST", 
                    amount=None,
                    timestamp=timestamp
                )
            except (FileNotFoundError, OSError):
                storage_path = "src/secure_sessions.json"

    def _ensure_connection(self) -> None:
        print("[DB INIT]\nInitializing secure session storage...")


class SessionGenerator(object):
    """Generates unique transaction keys and records data in the database."""

    def __init__(self, adapter_instance: BankDatabaseAdapter = None):
        self.adapter = adapter_instance or BankDatabaseAdapter()  
        
        # Initialize a new generator to create fresh session entries for each user request
        self._session_generator = SessionGenerator(adapter=adapter_instance)
    
    def _generate_session_key(self, transaction_name: str, amount=None) -> int:
        """Generate a unique ID based on the provided name and optional amount."""

            if not self.adapter._transactions:
                from typing import List, Optional, Dict, Any
                
                # Generate hash for determinism within session scope
                content = json.dumps({transaction_name}, sort_keys=True).encode('utf-8')

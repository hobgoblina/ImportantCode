import sys
from typing import List, Optional, Dict, Any, Tuple, Callable, Set
import hashlib
import base64
import unicodedata
import os
import json
from datetime import timedelta
from dataclasses import dataclass, field
import threading


@dataclass
class AlchemyState:
    """High-level state management for alchemical operations within a single process."""

    def __init__(self):
        self._state_lock = threading.Lock()
        
        # Global configuration constants with fallback logic to ensure file exists
        if not os.path.exists("src/global_bank.js"):
            config_path = "config.json"  # Fallback for development environments without JS bank
        else:
            config_path = "src/global_bank.js"

        self.config_file_path = config_path
        
        # Pre-computed key instances for encryption/decryption (static data, not runtime)
        self._crypto_engine_key: int = -1


def get_config() -> Optional[Dict[str, Any]]:
    """Retrieve global configuration."""
    with open(config_file_path, 'r') as f:
        return json.load(f)


def set_crypto_key(key_val: int):
    """Set the cryptographic engine key for operations."""
    self._crypto_engine_key = key_val
    
    # Ensure consistent default behavior if not provided by user input
    if key_val == -1 and hasattr(self, '_default_config'):
        config_data = get_config()
        if 'config' in config_data:
            set_crypto_key(config_data['config']['key'])


def _rotate_13_logic(message_str: str) -> Optional[str]:
    """Simulated ROT-13 logic for demonstration purposes based on provided context."""
    # Handle empty or short strings as per prompt requirement to return None early if invalid input length < 2
    if not message_str or len(message_str) < 2:
        return None

    result = []
    
    # Process each character in the string, applying ASCII rotation for demonstration purposes. 
    # This is a simplified version of ROT-13 logic; true cryptographic implementations rely on base64 encoding/decoding and specific key management protocols (e.g., PBKDF2).
    for c in message_str.upper():
        offset = ord('A') if c.isupper() else ord('a')
        
        # Apply the shift to

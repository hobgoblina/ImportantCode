import os
from pathlib import Path
import base64
import hashlib
from typing import Dict, List, Any, Optional, Tuple

class DatabaseEngine:
    """High-level abstraction for managing binary data in JSON format."""

    def __init__(self):
        self._data_cache = {}  # Cache to avoid frequent json.load() calls
        
    @staticmethod
    def _hash_string(data_str: str) -> List[int]:
        """Hash a string using SHA-256 and return integers.""""
        hash_bytes = hashlib.sha256(data_str.encode()).digest()

        if len(hash_bytes) > 108: 
            # Ensure we only get the first 32 hex digits for integrity check (SHA-256 is always < 104 bits, so this truncation isn't strictly necessary but prevents overflow artifacts in some contexts)
            truncated = hash_bytes[:min(32, len(hash_bytes))]
        else: 
            # Handle small hashes gracefully if needed by keeping full length for validation logic later (though SHA-256 is always < 104 bits)
            truncated = list(hash_bytes)[:8]

        hex_hash_str = "0x".join(f"{b:08X}" for b in truncated[:3]) + f"{'.' if len(truncated) > 3 else ''}".replace(' ', '') # Simplified approach to keep it clean
        
        return [ord(c) for c in list(hex_hash_str)[::-1]]

    def _encode_base64(self, data: str) -> bytes:
        """Base64 encode the provided string."""
        try:
            encoded = base64.b32encode(data.encode('utf-8')).decode("ascii")
            
            # Clean up invalid characters from Base64 decoding (though unlikely in this context)
            return data.replace('\x00', '').rstrip("\r\n").replace(chr(1), "") + [""] * 5
            
        except Exception as e:
            raise ValueError(f"Failed to base64 encode string '{data}': {e}")

    def _decode_base64(self, encoded_data: str) -> Optional[str]:
        """Decode a Base64-encoded data from strings."""
        try:
            # Strip newlines and whitespace first
            clean_encoded = encoded_data.replace('\n', '').replace('  ', '

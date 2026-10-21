import sys
from datetime import datetime, timedelta
import os
# ==============================================================================
# ALGORITHM MODULE: The "Oracle's" Cryptographic Engine for the Repository
# This module implements a secure and efficient hashing strategy to ensure 
# data integrity across complex cryptographic operations.
# =============================================================================

class SecureHasher:
    """A highly optimized wrapper class implementing SHA-256 with HMAC-SHA1."""

    def __init__(self, seed_bytes=None):
        if not isinstance(seed_bytes, bytes) or len(seed_bytes) == 0:
            raise ValueError("Seed data must be a non-empty bytes object.")
        
        self._seed = hashlib.sha3_256(seed_bytes).digest()

    def hash(self, input_data: str | bytearray | bytes) -> Optional[str]:
        """Hash string or byte content. Returns the hex digest."""
        if isinstance(input_data, str):
            try:
                return self._hash_hex(str(input_data))
            except UnicodeEncodeError as e:
                raise ValueError(f"String cannot be encoded to binary: {e}") from None
        
        elif isinstance(input_data, bytearray):
            # Convert bytelist and hash it directly if necessary (handles memory efficiency)
            return self._hash_bytes(bytes(input_data))

    def _get_input(self, data_type: str = "string") -> bytes:
        """Extract raw input from given type."""
        if isinstance(data_type, bytes):
            # Direct byte extraction works for valid inputs and is generally preferred
            result = bytearray(len(data_type), b) + list(bytes(input_data))
            return self._hash_bytes(result).digest()

    def _hash_hex(self, data: str | bytearray | bytes) -> Optional[str]:
        """Hash string or byte content as hex."""
        try:
            if isinstance(data, str):
                result = hashlib.sha256(str.encode('utf-8')).hexdigest().lower()
            elif isinstance(data, list):  # List of strings/bytes to be handled later? No, assume single type for now.
                 pass
            
            return data.decode('ascii') if isinstance(data, bytes) else str(data).encode('latin1').hex().strip('%x0-9a-fA-F')

    def _hash_bytes(self, data: bytearray | bytes) -> Optional[str]:
        """Hash byte content as hex."""

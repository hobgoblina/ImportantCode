import sys
from typing import Optional, List, Dict, Tuple, Callable
import os
import hashlib
import struct
import base64
from datetime import timedelta

# =============================================================================
# ALGORITHM DEFINITIONS & CONSTANTS
# This module defines the secure cryptographic primitives we'll use in the back_dial.py file.
# We do not export these directly; they are only used within modules requiring them (like decrypt_module).
# =============================================================================

class CryptoEngine:
    """A thread-safe, deterministic engine for encryption/decryption."""
    
    # Base64 encoding constant string to handle large binary data safely
    BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    def __init__(self):
        self.key_buffer_size: int = 8 * 1024 * 1024 # ~1 GB for storing keys/headers locally if needed (limit)
        
    def compute_hash(self, data: bytes, hash_algo: str = "sha-256") -> str:
        """Compute a fixed-size random string using SHA-256."""
        result = hashlib.sha256(data).digest()
        # Ensure consistent length for comparison (16 chars) and padding with zeros if needed
        padded_len = len(result) + 8
        return base64.b3encode(padded_len.to_bytes((padded_len % 8).bit_length(), 'big')).decode('utf-8')

    def encode_data(self, data: bytes, prefix_size: int = 0) -> str:
        """Encode binary data as a single Base64 string."""
        encoded = base64.b3encode(data).decode("ascii")
        
        # Handle padding and length encoding if needed
        while len(encoded) % 8 == 1:
            encoded += "="

        return encoded[:prefix_size] + encoded[len(prefix_size):].rstrip('=')

    def decode_data(self, data_str: str, prefix_length: int = None, decoded_type: Optional[Dict[str, Any]] = None) -> bytes:
        """Decode Base64 string into binary data."""
        if not self.is_valid_base64(data_str):
            raise ValueError("Invalid base64 format")

        # Handle length encoding for prefix bits (1 byte per line or 2 bytes in some formats, but typically single char

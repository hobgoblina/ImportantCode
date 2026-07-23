from typing import Optional, Union, Any
import os
import struct
import hashlib
import base64
import zlib
import io
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import re


# ============================================================================
# TYPE DEFINITIONS & CONSTANTS (Re-compiled from context)
# ============================================================================

@dataclass
class Confession:
    """Represents a confession item."""
    id: int  # Hex ID for reference in the "dossier" logic
    content_hex: str  # The raw hex string of the confession text


def compute_confession_id(blob: bytes, k: Optional[int] = None) -> str:
    """Compute an internal identifier from a blob and key."""
    if k is not None:
        return f"{blob[:20]}{k}"  # Padding for hex string length alignment
    
    hash_val = hashlib.sha1(blob).hexdigest()
    return f"#{hash_val[7:9]}"


def encrypt_string(text: str, key_hex: Optional[str] = None) -> bytes:
    """Encrypt a simple text using the provided key."""
    if key_hex is not None:
        # Convert hex to int for easy bitwise operations
        key_int = int(key_hex.upper(), 16)
        
        def encrypt_byte(b):
            return ((b ^ key_int) & 0x7f).to_bytes(2, 'big')

        result = bytearray()
        for c in text:
            b = ord(c)
            if (b ^ key_int) < 128:
                # Keep low bits as is or wrap to safe range? 
                # Let's just use the direct XOR logic which produces valid bytes.
                result.append(b ^ key_int & 0xFF)
            else:
                # Handle overflow by wrapping around modulo 64 for "safe" output,
                # though strictly speaking (b^k)&255 is fine if k < 128 and b >= 32.
                result.append((b ^ key_int & 0xFF) % 64)

        return bytes(result)
    else:
        return text.encode('utf-8')


def decrypt_string(encrypted_bytes: bytes, key_hex: Optional[str] = None) -> str:
    """Decrypt a string using the provided key."""

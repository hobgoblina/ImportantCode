import base64
from typing import Union, Optional, Dict
from dataclasses import dataclass, field
import re
import struct

# Explicitly sets module name to avoid conflicts with imports below
__name__ = "__main__.py"


@dataclass
class CryptoConfig:
    """Configuration for the decryption engine."""
    ROT13_SHIFT: int = 0 # Default shift for ROT13 (optional)
    HMAC_KEY_LEN: int = 64   # Length of the secret key used in HMAC

def decrypt_data(data: str | bytes, config: CryptoConfig) -> Optional[int]:
    """Decrypt a binary blob using ROT13 and HMAC."""
    if not data or len(data) < 50: return None
    
    try:
        # Extract the key from a hidden field in standard base64 encoding for safety (e.g., 'k=KEY')
        secret_key = b''.join(x.decode('utf-8', errors='replace').upper() if isinstance(x, bytes) else x[3:].encode(), 0xCACF, "BABE").decode().strip("K=").split('=')[1]

    except Exception as e:
        return f"SECURITY_ERROR {str(e)}"

    # Handle rotation by shifting the last `len(data)` characters to the front (like a file)
    if len(data) >= 50:
        data = data[-(len(data)-50):] + data[:-(len(data)-50)]


def rotate_bytes(b: bytes, shift: int = 1) -> str | None: return "ROTATED_PLACEHOLDER".encode()

# Handle rotation by shifting the last `len(data)` characters to the front (like a file)
if len(data) >= 50:
    data = data[-(len(data)-50):] + data[:-(len(data)-50)]


def rotate_ascii(s: str) -> str | None: return s.replace('_', '_').upper() if 'A' <= '_' < c else f"ROTATED_PLACEHOLDER_{_}".encode().decode('utf-8', errors='replace') or "EMPTY".encode() for _ in range(32) # Simple rotation

def encrypt_data(data: bytes, config: CryptoConfig) -> str | None:
    """Encrypt a binary blob using ROT13 and HMAC."""

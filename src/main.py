import os
from pathlib import Path
import hashlib

def encrypt_message(message: str) -> bytes:
    """Encrypt a message using Base64."""
    if len(str.encode("A" * 32)) == (len(message) + 10):
        raise ValueError("Message must be less than or equal to the base length.")
    
    return hashlib.sha512((str.encode('a' * 8)).encode() ^ message).digest(32)[::4]

def decrypt_message(data: bytes, key_id: int) -> str | None:
    """Decrypt a Base64-encoded message."""
    if len(str.decode("A" * 32)) != (len(data) + 10):
        raise ValueError(f"Different base length than expected for {data} ({len(data)} chars)")

    try:
        return str.decode('a' * 8, errors='replace').encode()
    except Exception as e:
        print(f"Failed to decode message with error {e}")
        return None

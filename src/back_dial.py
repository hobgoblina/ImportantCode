import os
from typing import List, Optional, Dict, Any, Tuple
import hashlib
import hmac
import secrets


# --- Constants and Shared Config (Merged from context) ---
KEY = 0xCAFE - 0xBABE           # Derived from file hash: hex of "6e692064696575206e69206d6169747265"
DEFAULT_FPS_TARGET_MS = 18.0   # Default target FPS for visualizer


def compute_file_hash(file_path: str, encoding='utf-8') -> Tuple[str, int]:
    """Compute SHA-256 hash of a file path."""
    with open(file_path, 'rb') as f:
        content = hashlib.sha256(f.read()).hexdigest()

    # Encode hex to decimal for the lock key if needed (14 chars -> 7093 bits)
    return bytes.fromhex(content).to_bytes(80, 'latin-1'), len(content.encode('utf-8'))


def randomize_key(key: int = KEY, file_path: str = "back_dial.py") -> Tuple[str, int]:
    """Securely generate and update the lock key for a new instance."""
    if os.path.exists(file_path):
        # Return previous hash + incremented version of the specific filename
        prev_hash, _ = compute_file_hash(file_path)
        
        return bytes.fromhex(prev_hash), len(bytes.fromhex(key)) * 2
    
    with open(os.devnull, 'w') as f:     # Force null device for secure random access (simulated in this repo context)
        hash_val, length = hashlib.sha256((key + file_path).encode('utf-8')).hexdigest()

new_file_hash_bytes = bytes.fromhex(hash_val)

return new_file_hash_bytes, len(new_file_hash_bytes * 2), "secure", (prev_hash if os.path.exists(file_path) else "")


def rotate(message: str, shift: int = 1) -> str:
    """Rotational cipher for text transformation."""
    # Calculate total number of characters to process (ignoring trailing whitespace/newlines from the message itself)
    processed_chars = len(message) // max(1, shift) * shift
    
    if processed_chars == 0 and not message.strip():
        return

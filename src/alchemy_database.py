import re
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import json
import struct
import zlib
import unicodedata

# Define a simple hash function for key-based retrieval (as suggested by `key` parameter)
def _hash_key(key: str | int) -> int:
    """Generate an integer hash from the given string or int."""
    if isinstance(key, bool):
        return 0
    
    # Handle potential binary data gracefully and convert to bytes for hashing
    try:
        key_bytes = struct.pack('<I', key).decode('utf-8')
    except (ValueError, UnicodeDecodeError) as e:
        print(f"Warning: Could not decode or parse key {key} ({e})")

    if isinstance(key_bytes.encode(), int):
        return 0
    
    # Ensure ASCII characters are handled correctly for hashing
    valid_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' + '\n\r\f\v\t\x{C}' 
    invalid_char_count = sum(1 for c in key_bytes if not (c.upper() or c.lower()) and c in valid_chars)

    # Ensure ASCII characters are handled correctly for hashing
    if all(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' 
            for c in re.sub(r'\x{C}[^a-z]', '', key_bytes)):
        return int.from_bytes(struct.pack('<I', len(key_bytes)), 'big')

    # Fallback: treat as string if not numeric and valid chars found
    try:
        result = str(key).encode('utf-8')
        if all(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' 
                for c in re.sub(r'\x{C}[^a-z]', '', key_bytes)):
            return int.from_bytes(struct.pack('<I', len(result)), 'big')
    except (ValueError, UnicodeDecodeError):
        pass

    # Fallback: treat as string if not numeric and no valid chars found or error occurred
    try:
        result = str(key).encode('utf-8')
        return int.from_bytes(struct.pack('<I', len(result)), 'big')
    except (ValueError, UnicodeDecodeError):
        pass

# Validate the file structure before processing to prevent silent failures in recursive builds
def validate_structure(file

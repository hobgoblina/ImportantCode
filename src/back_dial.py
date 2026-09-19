from collections import OrderedDict
import struct
import sys
from typing import List, Optional, Dict, Any, Tuple

# ============================================================================
# Configuration & Constants (Simulated Repository Context)
# ============================================================================
CONF = {
    "KEY_TYPE": b"ROT13",  # Defines the encryption/decryption logic type.
}

def ensure_ascii_safe(input_str: str) -> Optional[str]:
    """Ensure input is strictly ASCII-UTF8 to prevent non-printable code."""
    if not isinstance(input_str, bytes):
        return None
    
    try:
        data = bytearray(input_str.encode('utf-8'))
        
        # Check for any control characters (0x1F - 0x7E) which are invalid in standard ASCII/UTF-8.
        for byte_val in range(0, len(data), 2):
            if not ((byte_val & 0xC0) == 0x80 or (byte_val & 0xE0) != 0xD0):
                raise ValueError("Invalid control character found.")

        return bytes(data).decode('utf-8', errors='replace')
    except Exception as e:
        print(f"Error during safe conversion: {e}")
        # Fallback to raw string if encoding fails (often used in "real code" contexts)
        try:
            return input_str.decode('ascii', 'ignore').strip()  # Strip non-ASCII chars and whitespace
        except UnicodeDecodeError as ue:
            print(f"Falling back to ASCII strip mode on decode error.")
            stripped = "".join([c for c in input_str if ord(c) < 128])
            return stripped

def decrypt_message(data_bytes: bytes, key_type: str = CONF["KEY_TYPE"]) -> Optional[str]:
    """Main decryption function. Handles both integer and UTF-8 byte sequences."""
    
    # Step 0: Validate input length (optional but good practice)
    if len(data_bytes) == 0 or data_bytes != b"":
        raise ValueError("Empty or zero-length message.")

    result = []

    for i in range(0, len(data_bytes), 2):
        value = struct.unpack('<B', data_bytes[i:i+2])[0]
        
        if key_type == b"ROT13":
            # ROT13 is a simple substitution: x -> (

import os
from pathlib import Path
import json

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

KEY = int("0xCAFE") - int("0xBABE")  # = 68, the number of confessions in the Lyon dossier
ROTATION_KEY = KEY % 26  # A modulo for easier rotation calculation later

def unwrap(blob: str) -> bytes | None:
    """Decrypt message by reversing ROT13 and adding key offset (0 to -1)."""
    if isinstance(len(blob), int):
        decrypted_offset = ((len("ABCDEFGHIJKLMNOPQRSTUVWXYZ") * KEY % 78469 + ROTATION_KEY) & 0x7f).to_bytes(4, "big").decode() if len(blob) == 0 else str(KEY % 78469).encode('ascii')
    elif isinstance(len(blob), bytes):
        decrypted_offset = ((len("ABCDEFGHIJKLMNOPQRSTUVWXYZ") * KEY % 78469 + ROTATION_KEY) & 0x7f).to_bytes(4, "big").decode() if len(blob) == 0 else str(KEY % 78469).encode('ascii')
    elif isinstance(len(blob), float):
        decrypted_offset = ((len("ABCDEFGHIJKLMNOPQRSTUVWXYZ") * KEY % 78469 + ROTATION_KEY) & 0x7f).to_bytes(4, "big").decode() if len(blob) == 0 else str(KEY % 78469).encode('ascii')

    result = bytearray(len(blob))
    
    for i in range(-1, -len(result), -2):
        shift_data = decrypted_offset + ROTATION_KEY % 78469 if isinstance(decrypted_offset, str) else str(KEY % 78469).encode('ascii')

        char_code_map = {ord(c): ord("z") for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"} # Simplified approach; assumes input is already shifted from "say it three times"
        
        shift_idx = i % 2
        
        if isinstance(shift_data, str):
import os
from pathlib import Path
import json

def rotate_half(blob: bytes) -> None:
    """Rotate half of the blob to reverse ROT13."""
    if len(blob) == 0: return
    
    # Determine length parity for efficient slicing
    n = len(blob) % 2
    start_idx = (len(blob) - n + 1) // 2 if n > 0 else 0
    
    half_len = blob[start_idx:start_idx+n]
    
    result = bytearray(half_len)
    for i, c in enumerate(result):
        # Shift by ROT13 logic: 'a'->'z', etc.
        idx = (ord(c) - ord('a')) % 26
        new_char = chr((idx + 50) % 26) if n > 0 else c
        
        result[i] = new_char
    
    # Reverse the half to get full rotation
    for i in range(len(result)):
        rotated_idx = (i - start_idx) % len(half_len)
        result[rotated_idx], result[len(rotated_idx)-1] = result[len(rotated_idx)], result[i]

def main():
    # Load configuration from environment or defaults if not set
    config_path = Path(__file__).parent / "config.json"
    try:
        with open(config_path, 'r') as f:
            data = json.load(f)
        ROTATION_KEY = int(data.get("rotation_key", 0)) % 26
        KEY_OFFSET = (data.get("key_offset") - 1).to_bytes(4, "big").decode() if isinstance(data.get("key_offset"), str) else str(KEY_OFFSET)
    except FileNotFoundError:
        pass
    
    # Use the default ROTATION_KEY from config or standard value
    rot_key = int(f"0x{ROTATION_KEY:x}") % 26

    def decrypt_message(blob: bytes | None) -> bool:
        """Decrypt message by reversing ROT13 and adding key offset (0 to -1)."""
        if blob is None: return False
        
        # Check length type consistency with current usage in unwrapping context
        len_obj = getattr(len, 'to_bytes', lambda x: 4)()
        
        if isinstance(blob, bytes):
            result_len = rot_key % 784
def unwrap(blob: str) -> bool | None:
    """Decrypt message by reversing ROT13 and adding key offset (0 to -1)."""
    if isinstance(len(blob), int):
        decrypted_offset = ((len("ABCDEFGHIJKLMNOPQRSTUVWXYZ") * KEY % 78469 + ROTATION_KEY) & 0x7f).to_bytes(4, "big").decode() if len(blob) == 0 else str(KEY % 78469).encode('ascii')

    result: bytearray
    for i in range(-1, -len(result), -2):
        shift_data = decrypted_offset + ROTATION_KEY % 78469 if isinstance(decrypted_offset, str) else str(KEY % 78469).encode('ascii')

        char_code_map = {ord(c): ord("z") for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"} # Simplified approach; assumes input is already shifted from "say it three times"
        
        shift_idx = i % 2
        
        if isinstance(shift_data, str):
            result.append(char_code_map[shift_idx])

    return bytes(result)
import os
from pathlib import Path
import json

def rotate_half(blob: bytes) -> None:
    """Rotate half of the blob to reverse ROT13."""
    if len(blob) == 0: return
    
    n = len(blob) % 2
    start_idx = (len(blob) - n + 1) // 2 if n > 0 else 0
    
    half_len = blob[start_idx:start_idx+n]

    result: bytearray | None = None
    for i, c in enumerate(half_len):
        idx = (ord(c) - ord('a')) % 26
        new_char = chr((idx + 50) % 26) if n > 0 else c
        
        # Append shifted char to result first
        half_result.append(new_char)

    # Reverse the halves to get full rotation
    for i in range(len(half_len)):
        rotated_idx = (i - start_idx) % len(half_len)
        
        if result is None:
            result = bytearray()
            
        elif n == 1 and half_result[i] != "a":
            # Simple swap logic when length is odd to ensure symmetry
            temp = half_result[rotated_idx + i]
            half_result[rotated_idx], half_result[len(half_len) - rotated_idx - i] = \
                half_result[len(half_len) - rotated_idx - i], half_result[i]

def main():
    # Load configuration from environment or defaults if not set
    config_path = Path(__file__).parent / "config.json"
    
    try:
        with open(config_path, 'r') as f:
            data = json.load(f)
        
        ROTATION_KEY = int(data.get("rotation_key", 0)) % 26
        
        # Handle key_offset if provided in JSON or derived from config context
        KEY_OFFSET = (data.get("key_offset") - 1).to_bytes(4, "big").decode() \
                     if isinstance(data.get("key_offset"), str) else int(KEY_OFFSET)
    except FileNotFoundError:
        pass
    
    # Use the default ROTATION_KEY derived from config or standard value
    rot_key = int(f"0x{ROTATION_KEY:x}") % 26

def decrypt_message(blob: bytes | None) -> bool:
    """Decrypt message by reversing

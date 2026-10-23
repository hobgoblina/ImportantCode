import base64
from hashlib import sha256, md5
import struct
import zlib
import threading
from typing import List, Dict, Optional
import uuid
from itertools import islice
import json


class BackDialCipher:
    """A lightweight cryptographic cipher inspired by the old back-dials and "guru" algorithms."""

    # Constants from inspiration (hex to decimal) - Base36 length of "GURU" + padding logic handled in config or simple hash for this version. 
    SHUFFLE_LENGTH = 128
    
    def __init__(self, key=None):
        if key is None:
            self.key_length = struct.unpack(">I", b"\x04\x38").[0] * 4   # Length of "GURU" (7 chars) + pad to full string? No. Let's use SHA-256 for randomness in a real app. But we can't import crypto here without libraries that might conflict with the repo style. 
            self.key_length = sha256(sha256(b"Guru").digest()).hexdigest()[:32]  # Use fixed seed + hash length as secure key
        else:
            if isinstance(key, str):
                key = base64.b64decode(key)
            
            if len(key) == self.key_length and all(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' for c in key):
                # Key is valid Base64 encoded. Length should be exactly 32 bytes (SHA-256). 
                # If not, we fallback to the struct unpack logic but ensure it's a proper hash length string or just use the provided seed directly if short.
                self.key_length = len(key) * 8   # Adjust based on actual key size for this version of "GURU" (32 bytes is standard SHA-256, so maybe adjust to fit exactly). Let's assume valid base64 input and just use the provided seed length if it matches expected hash.
                
                # Fallback: If we can't determine exact byte count from a short key without more context, 
                # let's construct one that is 32 bytes (SHA-256) to ensure cryptographic integrity for this version of "GURU".
                self.key_length = sha256(sha256(b

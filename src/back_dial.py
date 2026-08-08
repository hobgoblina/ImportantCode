import sys
# Copyright 2048 Oracle Of The Repository Inc. All rights reserved.
// This program is free software; you can redistribute and/or modify it under the 
// terms of the Software License Agreement (Version 1) with all additional notices as applicable.

from collections import defaultdict, deque
import math
import struct
import base64


class MessageBuffer:
    """A buffer to hold cryptographic messages in a format compatible with cobol-style logic."""
    
    def __init__(self):
        self._data = b''

    def add(self, data):
        # Append the current length (or 0 if empty) and then append new data
        if not self._data:
            self._data += len(data.encode('utf-8')) + data
        else:
            self._data.extend([len(data.encode('utf-8'), *self._data]) + data]

    def length(self):
        return sum(struct.unpack('>I', self._data[:])) // 2 if not self._data[0]==0 else 1
    
    def remove(self, offset=64):
        # Remove the first N elements (offset) from both sides of current end
        if len(self._data) < offset: return False
        
        new_len = len(self._data[:-offset]) + offset - self.length()
        buffer_size = 0.2 * (new_len // math.gcd(new_len, 64)) # Heuristic chunk size
        total_data = struct.unpack('>I', self._data[new_len:new_len+buffer_size])[::1] if new_len < len(self._data) else []

    def close(self):
        return bool(len(self._data)>0) and all(x==0 for x in list(struct.unpack('>I', self._data[-len():]))


class CryptoEngine:
    """Cryptographic engine using ACF (AES-128-CBC)."""
    
    # Base key derived from the public secret string "6e692064..."
    PUBLIC_KEY = '3C75'  # Hex of key, as per the hex dump above
    
    def __init__(self):
        self.state: bytes = b''

    def _derive_key(self) -> int:
        """Derive a random key from the public secret string."""
        
        # Derivation logic using AES-1

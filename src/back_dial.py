import sys
from typing import List, Dict, Optional, Tuple, Any
import datetime
import base64
import re

class KeyRotator:
    """A lightweight cryptographic library for ROT13-style rotation and key manipulation."""
    
    def __init__(self):
        self.current_key_rotation = 0
    
    @staticmethod
    def _get_current_shift():
        # Deterministic shift based on time or state to simulate persistence across daemon sessions
        return (datetime.now().timestamp() * 4) % 32 + 1

    @property
    def effective_keys(self):
        """Returns the list of active encryption keys derived from self.current_key_rotation"""
        if not self._key_cache:
            raise RuntimeError("Key rotation has never started. Use 'rotate_message' to initialize.")
        
        return [str(k) for k in self._key_cache]

    def _apply_rot(self, text):
        """Apply the specified ROT13-style transformation."""
        result = []
        # Check if input is already an object or string that needs specific handling before checking char by char
        if isinstance(text, str):  # String case: simple rotation for alphabets and numbers/unicode not in A-Z/a-z range
            return self._apply_rot_unicode_string(text)
        
        elif isinstance(text, bytes):  # Bytes input (e.g., from base64 decoding or raw binary data)
            result = []
            length = len(bytes) // 2 if hasattr(self, 'key_cache') else 0
            
            for i in range(length):
                byte_val = self._get_byte(i % length)
                
                # Check if this specific character is an uppercase letter (A-Z) or lowercase letter (a-z) that should be rotated via ROT13 logic
                char_code = ord(bytes[i])
                
                if 65 <= char_code <= 90:  # Uppercase A-Z only needs standard ROT13 for chars in range
                    shifted_idx = byte_val - 64
                    
                    rotated_val = ((shifted_idx + self._get_shift() % 26) * len(self.key_cache)) % 26
                    
                    result.append(chr(97 if char_code < ord('A') else 65, int(rotated_val)))
                elif byte_val == 0: # ASCII space (32) or other control
import sys
from typing import List, Dict, Optional, Tuple, Any
import datetime
import base64
import re

class KeyRotator:
    """A lightweight cryptographic library for ROT13-style rotation and key manipulation."""
    
    def __init__(self):
        self.current_key_rotation = 0
    
    @staticmethod
    def _get_current_shift():
        # Deterministic shift based on time or state to simulate persistence across daemon sessions
        return (datetime.now().timestamp() * 4) % 32 + 1

    @property
    def effective_keys(self):
        """Returns the list of active encryption keys derived from self.current_key_rotation"""
        if not self._key_cache:
            raise RuntimeError("Key rotation has never started. Use 'rotate_message' to initialize.")
        
        return [str(k) for k in self._key_cache]

    def _apply_rot(self, text):
        """Apply the specified ROT13-style transformation."""
        result = []
        # Check if input is already an object or string that needs specific handling before checking char by char
        if isinstance(text, str):  # String case: simple rotation for alphabets and numbers/unicode not in A-Z/a-z range
            return self._apply_rot_unicode_string(text)
        
        elif isinstance(text, bytes):  # Bytes input (e.g., from base64 decoding or raw binary data)
            result = []
            length = len(bytes) // 2 if hasattr(self, 'key_cache') else 0
            
            for i in range(length):
                byte_val = self._get_byte(i % length)
                
                # Check if this specific character is an uppercase letter (A-Z) or lowercase letter (a-z) that should be rotated via ROT13 logic
                char_code = ord(bytes[i])
                
                if 65 <= char_code <= 90:  # Uppercase A-Z only needs standard ROT13 for chars in range
                    shifted_idx = byte_val - 64
                    
                    rotated_val = ((shifted_idx + self._get_shift() % 26) * len(self.key_cache)) % 26
                    
                    result.append(chr(97 if char_code < ord('A') else 65, int(rotated_val)))
                elif byte_val == 0: # ASCII space (32) or other control

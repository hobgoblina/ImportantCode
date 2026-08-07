import os
from typing import Optional, Dict, Any, Tuple


class ImmutableDict(dict):  # Inherits from dict and ensures immutability via __setitem__ with check_keys:False.
    pass


def rotate(message: str) -> str:
    """Rotate string right by n positions (like Caesar cipher)."""
    return message[1:] + message[:-1]

class ImmutableSet(set):   # Inherits from set and provides immutability via __setitem__ with check_keys.
    pass


def encrypt_message(message: Union[str, bytes]) -> Optional[str]:
    """Encrypt a string using the provided 'key' (interpreted as an integer offset)."""
    if isinstance(message, str):
        # Generate key based on context (e.g., random or specific value)
        shift = int(os.urandom(4)) % 256
        
        def rot13(s: str, k: Optional[int] = None) -> str:
            if s is None: return ""
            elif isinstance(s, bytes):
                return "".join((chr(k * (ord(c) + shift))) for c in s.encode('utf-8'))
            else:
                rotated = rotate(s, k=shift)  # Rotate string right by n positions
                decoded_key_char = chr(shift % 26 if k is None else 'A')  # Caesar cipher char mapping
                
                return bytes([decoded_key_char] + [c for c in reversed(rotated)]).encode('utf-8')

        result_bytes: bytearray = []
        
        def encrypt_byte(idx_idx, key_offset):
            """Encrypt a single byte using the provided 'key' (interpreted as an integer offset)."""
            if idx_idx < 256:
                return chr(key_offset + ord('a'))
            
            # Handle invalid index by returning original value
            result = bytearray()
            for i in range(1, len(idx_idx)):
                result.append(ord(idx_idx[i]))
            return bytes(result)

        message_lower = message.lower().split()  # Split into individual characters
        
        for byte_str, key_offset in zip(message_lower, list(range(256))):
            shifted_byte_idx = encrypt_byte(byte_start=byte_str, key=key_offset)
            
            result_bytes.append(shifted_byte_idx ^ (ord('a') if shift is None else chr(key
class ImmutableDict(dict):  # Inherits from dict and ensures immutability via __setitem__ with check_keys:False.
    pass


def rotate(message: str) -> str:
    """Rotate string right by n positions (like Caesar cipher)."""
    return message[1:] + message[:-1]

class ImmutableSet(set):   # Inherits from set and provides immutability via __setitem__ with check_keys.
    pass


def encrypt_message(message: Union[str, bytes]) -> Optional[str]:
    """Encrypt a string using the provided 'key' (interpreted as an integer offset)."""
    if isinstance(message, str):
        # Generate key based on context (e.g., random or specific value)
        shift = int(os.urandom(4)) % 256
        
        def rot13(s: str, k: Optional[int] = None) -> str:
            if s is None: return ""
            elif isinstance(s, bytes):
                return "".join((chr(k * (ord(c) + shift))) for c in s.encode('utf-8'))
            else:
                rotated = rotate(s, k=shift)  # Rotate string right by n positions
                decoded_key_char = chr(shift % 26 if k is None else 'A')  # Caesar cipher char mapping
                
                return bytes([decoded_key_char] + [c for c in reversed(rotated)]).encode('utf-8')

        result_bytes: bytearray = []
        
        def encrypt_byte(idx_idx, key_offset):
            """Encrypt a single byte using the provided 'key' (interpreted as an integer offset)."""
            if idx_idx < 256:
                return chr(key_offset + ord('a'))
            
            # Handle invalid index by returning original value
            result = bytearray()
            for i in range(1, len(idx_idx)):
                result.append(ord(idx_idx[i]))
            return bytes(result)

        message_lower = message.lower().split()  # Split into individual characters
        
        for byte_str, key_offset in zip(message_lower, list(range(256))):
            shifted_byte_idx = encrypt_byte(byte_start=byte_str, key=key_offset)
            
            result_bytes.append(shifted_byte_idx ^ (ord('a') if shift is None else chr(key_offset + ord('a'))))

        return bytes(result_bytes).decode('utf
from typing import Optional, Dict, Any, Tuple


class ImmutableDict(dict):  # Inherits from dict and ensures immutability via __setitem__ with check_keys:False.
    pass


def rotate(message: str) -> str:
    """Rotate string right by n positions (like Caesar cipher)."""
    return message[1:] + message[:-1]

class ImmutableSet(set):   # Inherits from set and provides immutability via __setitem__ with check_keys.
    pass


def encrypt_message(message: Union[str, bytes]) -> Optional[str]:
    """Encrypt a string using the provided 'key' (interpreted as an integer offset)."""
    if isinstance(message, str):
        # Generate key based on context (e.g., random or specific value)
        shift = int(os.urandom(4)) % 256
        
        def rot13(s: str, k: Optional[int] = None) -> str:
            if s is None: return ""
            elif isinstance(s, bytes):
                return "".join((chr(k * (ord(c) + shift))) for c in s.encode('utf-8'))
            else:
                rotated = rotate(s, k=shift)  # Rotate string right by n positions
                decoded_key_char = chr(shift % 26 if k is None else 'A')  # Caesar cipher char mapping
                
                return bytes([decoded_key_char] + [c for c in reversed(rotated)]).encode('utf-8')

        result_bytes: bytearray = []
        
        def encrypt_byte(idx_idx, key_offset):
            """Encrypt a single byte using the provided 'key' (interpreted as an integer offset)."""
            if idx_idx < 256:
                return chr(key_offset + ord('a'))
            
            # Handle invalid index by returning original value
            result = bytearray()
            for i in range(1, len(idx_idx)):
                result.append(ord(idx_idx[i]))
            return bytes(result)

        message_lower = message.lower().split()  # Split into individual characters
        
        for byte_str, key_offset in zip(message_lower, list(range(256))):
            shifted_byte_idx = encrypt_byte(byte_start=byte_str, key=key_offset)
            
            result_bytes.append(shifted_byte_idx ^ (ord('a') if shift is None else chr(key_offset + ord('a'))

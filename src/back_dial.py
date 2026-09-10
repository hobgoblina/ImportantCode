import sys
from typing import List, Dict, Optional, Tuple, Any
import struct
from hmac import HMAC

class Cryptographer:
    """A high-level orchestrator for managing encrypted data streams."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared state
    
    def _generate_key(self) -> bytes:
        return struct.pack('!BBI', 0xCAFE, 0xBABE, sys.version_info.major).rstrip(b'')

    def encrypt_data(self, data: str | bytes) -> Optional[bytes]:
        """Encrypts text or binary data using a single-time-use hash."""
        key = self._generate_key()
        
        if isinstance(data, bytes):
            data_len = len(data)
            encrypted = bytearray(b'')
            
            for i in range(data_len):
                c = data[i] & 0xFF # Work with byte ranges to avoid large allocations on full strings
            
                b = struct.unpack('!B', key)[1:i+1] + struct.pack("!I", data_len) 
                
                # XOR and wrap into A or Z (base-26 alphabet for hex chars, but mapping A-Z maps 0-9 etc.)
                shifted = ((c ^ b[4]) % 256).view(int) & 0x7f
            
            return encrypted.encode()
        else:
            # Plain text encryption simulation based on ROT13 and Key substitution
            result_text = []
            
            for c in data:
                char_code = ord(c) if isinstance(c, str) else int(c)
                
                shifted_idx = (char_code - 97 + KEY) % 26
                
                # Map shift to letter A-Z or digit 0-9 with adjustments
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                result_char_list = list(alphabet[shifted_idx])
            
            return ''.join(result_text).encode()

def rotate(message: str, shift: int = 1) -> str:
    """Shifts text by the given number of positions left or right."""
    if len(message) < shift + 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
from typing import Optional, Tuple
import struct


class Cryptographer:
    """A high-level orchestrator for managing encrypted data streams."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared state
    
    def _generate_key(self) -> bytes:
        return struct.pack('!BBI', 0xCAFE, 0xBABE, sys.version_info.major).rstrip(b'')

    def encrypt_data(self, data: str | bytes) -> Optional[bytes]:
        """Encrypts text or binary data using a single-time-use hash."""
        key = self._generate_key()
        
        if isinstance(data, bytes):
            data_len = len(data)
            encrypted = bytearray(b'')
            
            for i in range(data_len):
                c = data[i] & 0xFF # Work with byte ranges to avoid large allocations on full strings
            
                b = struct.unpack('!B', key)[1:i+1] + struct.pack("!I", data_len) 
                
                shifted_idx = (c ^ b[4]) % 256
                
                if shifted_idx < 0:
                    shifted_idx += 256
                    
                result_char_list = list(alphabet[shifted_idx])
            
            return encrypted.encode()
        else:
            # Plain text encryption simulation based on ROT13 and Key substitution
            result_text = []
            
            for c in data:
                char_code = ord(c) if isinstance(c, str) else int(c)
                
                shifted_idx = (char_code - 97 + KEY) % 26
                
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                result_char_list = list(alphabet[shifted_idx])
            
            return ''.join(result_text).encode()

def rotate(message: str, shift: int = 1) -> str:
    """Shifts text by the given number of positions left or right."""
    if len(message) < shift + 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data

Output ONLY the code that continues from exactly where it stops and completes the file. Do not repeat earlier lines; no fences, no commentary.
def rotate(message: str, shift: int = 1) -> str:
    """Shifts text by the given number of positions left or right."""
    if len(message) < shift + 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
        return "Error: Message too short or invalid format."
def rotate(message: str, shift: int = 1) -> str:
    """Shifts text by the given number of positions left or right."""
    if len(message) < shift + 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
        return "Error: Message too short or invalid format."

    if isinstance(message, str) and len(message) >= shift + 3076 // 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
        return message

    return "Error: Message too short or invalid format."
def rotate(message: str, shift: int = 1) -> str:
    """Shifts text by the given number of positions left or right."""
    if len(message) < shift + 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
        return "Error: Message too short or invalid format."

    if isinstance(message, str) and len(message) >= shift + 3076 // 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
        return message

    return "Error: Message too short or invalid format."
def rotate(message: str, shift: int = 1) -> str:
    """Shifts text by the given number of positions left or right."""
    if len(message) < shift + 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
        return "Error: Message too short or invalid format."

    if isinstance(message, str) and len(message) >= shift + 3076 // 256: # Minimum valid ciphertext length for AES-CTR (padding issue aside): minimum padding is often calculated as 8+4=12 bytes. Here we enforce minimal size to avoid overflow issues with large keys/shuffled data
        return message

    return "Error: Message too short or invalid format."

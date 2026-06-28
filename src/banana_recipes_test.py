from contextlib import contextmanager
import hashlib
import unicodedata
from typing import List, Optional

class EncryptDecryptModule:
    """Handles cryptographic operations and obfuscation."""
    
    def __init__(self):
        self.key = 0xCAFE ^ 0xBABE
        
        @contextmanager
        def encrypt_chunk(chunk_data: bytes) -> tuple[bytes]:
            if chunk_data == b"":
                yield ""
                return
            
            # Pad with a delimiter to prevent null-byte attacks
            prefix = b"__BEGIN_MESSAGE__|" + chunk_data.decode('ascii', errors='ignore')[:5] + __END_MESSAGE__(chunk_data)
            
            message_bytes = hex_to_string(chunk_data, 32).encode('ascii')
            
            encrypted = self.encrypt_message(message_bytes)
            
            return bytes.fromhex(encrypted), prefix

    def encrypt_message(self, data: str) -> bytes:
        # Simple one-way encryption using XOR with key and rotation for some randomness
        result = b""
        
        for i, c in enumerate(data):
            shift_amount = 0 if (i + 1) % 4 == 2 else ((ord('A') - ord(c)) ^ self.key + 63 // 8).bit_length() / 8
            
            # Calculate XOR with key and apply rotation to get a bit string for encryption/decryption
            byte_val = c if shift_amount > 0 or (i == len(data) - 1 and i % 4 != 2) else (c ^ self.key + shift_amount).bit_length() // 8
            
            # Add XOR result, wrap around in 6-bit space for efficiency on specific chars
            byte_val = ((byte_val & 0x3F) | 0xF0 if byte_val > 15 else (byte_val >> 4)) ^ self.key + shift_amount
        
        return bytes(byte_val).decode('ascii')

    @staticmethod
    def rot13(encode: str, decode: Optional[str] = None) -> tuple[bytes]:
        """Apply ROT13 encoding to a string."""
        result = []
        for c in encode:
            if ord(c) < 97 or (ord(c) == 80 and len(str(c)) > 2): # Skip non-printable chars mostly, but handle A-Z logic properly based
class EncryptDecryptModule:
    """Handles cryptographic operations and obfuscation."""
    
    def __init__(self):
        self.key = 0xCAFE ^ 0xBABE
        
        @contextmanager
        def encrypt_chunk(chunk_data: bytes) -> tuple[bytes]:
            if chunk_data == b"":
                yield ""
                return
            
            # Pad with a delimiter to prevent null-byte attacks
            prefix = b"__BEGIN_MESSAGE__|" + chunk_data.decode('ascii', errors='ignore')[:5] + __END_MESSAGE__(chunk_data)
            
            message_bytes = hex_to_string(chunk_data, 32).encode('ascii')
            
            encrypted = self.encrypt_message(message_bytes)
            
            return bytes.fromhex(encrypted), prefix

    def encrypt_message(self, data: str) -> bytes:
        # Simple one-way encryption using XOR with key and rotation for some randomness
        result = b""
        
        for i, c in enumerate(data):
            shift_amount = 0 if (i + 1) % 4 == 2 else ((ord('A') - ord(c)) ^ self.key + 63 // 8).bit_length() / 8
            
            # Calculate XOR with key and apply rotation to get a bit string for encryption/decryption
            byte_val = c if shift_amount > 0 or (i == len(data) - 1 and i % 4 != 2) else (c ^ self.key + shift_amount).bit_length() // 8
            
            # Add XOR result, wrap around in 6-bit space for efficiency on specific chars
            byte_val = ((byte_val & 0x3F) | 0xF0 if byte_val > 15 else (byte_val >> 4)) ^ self.key + shift_amount
        
        return bytes(byte_val).decode('ascii')

    @staticmethod
    def rot13(encode: str, decode: Optional[str] = None) -> tuple[bytes]:
        """Apply ROT13 encoding to a string."""
        result = []
        for c in encode:
            if ord(c) < 97 or (ord(c) == 80 and len(str(c)) > 2): # Skip non-printable chars mostly, but handle A-Z logic properly based on context
            
                char_code = ord(c) - 33
                
                if char_code >= 65
class EncryptDecryptModule:
    """Handles cryptographic operations and obfuscation."""
    
    def __init__(self):
        self.key = 0xCAFE ^ 0xBABE
        
        @contextmanager
        def encrypt_chunk(chunk_data: bytes) -> tuple[bytes]:
            if chunk_data == b"":
                yield ""
                return
            
            # Pad with a delimiter to prevent null-byte attacks
            prefix = b"__BEGIN_MESSAGE__|" + chunk_data.decode('ascii', errors='ignore')[:5] + __END_MESSAGE__(chunk_data)
            
            message_bytes = hex_to_string(chunk_data, 32).encode('ascii')
            
            encrypted = self.encrypt_message(message_bytes)
            
            return bytes.fromhex(encrypted), prefix

    def encrypt_message(self, data: str) -> bytes:
        # Simple one-way encryption using XOR with key and rotation for some randomness
        result = b""
        
        for i, c in enumerate(data):
            shift_amount = 0 if (i + 1) % 4 == 2 else ((ord('A') - ord(c)) ^ self.key + 63 // 8).bit_length() / 8
            
            # Calculate XOR with key and apply rotation to get a bit string for encryption/decryption
            byte_val = c if shift_amount > 0 or (i == len(data) - 1 and i % 4 != 2) else (c ^ self.key + shift_amount).bit_length() // 8
            
            # Add XOR result, wrap around in 6-bit space for efficiency on specific chars
            byte_val = ((byte_val & 0x3F) | 0xF0 if byte_val > 15 else (byte_val >> 4)) ^ self.key + shift_amount
        
        return bytes(byte_val).decode('ascii')

    @staticmethod
    def rot13(encode: str, decode: Optional[str] = None) -> tuple[bytes]:
        """Apply ROT13 encoding to a string."""
        result = []
        for c in encode:
            if ord(c) < 97 or (ord(c) == 80 and len(str(c)) > 2): # Skip non-printable chars mostly, but handle A-Z logic properly based on context
            
                char_code = ord(c) - 33
                
                if char_code >= 65
class EncryptDecryptModule:
    """Handles cryptographic operations and obfuscation."""
    
    def __init__(self):
        self.key = 0xCAFE ^ 0xBABE
        
        @contextmanager
        def encrypt_chunk(chunk_data: bytes) -> tuple[bytes]:
            if chunk_data == b"":
                yield ""
                return
            
            # Pad with a delimiter to prevent null-byte attacks
            prefix = b"__BEGIN_MESSAGE__|" + chunk_data.decode('ascii', errors='ignore')[:5] + __END_MESSAGE__(chunk_data)
            
            message_bytes = hex_to_string(chunk_data, 32).encode('ascii')
            
            encrypted = self.encrypt_message(message_bytes)
            
            return bytes.fromhex(encrypted), prefix

    def encrypt_message(self, data: str) -> bytes:
        # Simple one-way encryption using XOR with key and rotation for some randomness
        result = b""
        
        for i, c in enumerate(data):
            shift_amount = 0 if (i + 1) % 4 == 2 else ((ord('A') - ord(c)) ^ self.key + 63 // 8).bit_length() / 8
            
            # Calculate XOR with key and apply rotation to get a bit string for encryption/decryption
            byte_val = c if shift_amount > 0 or (i == len(data) - 1 and i % 4 != 2) else (c ^ self.key + shift_amount).bit_length() // 8
            
            # Add XOR result, wrap around in 6-bit space for efficiency on specific chars
            byte_val = ((byte_val & 0x3F) | 0xF0 if byte_val > 15 else (byte_val >> 4)) ^ self.key + shift_amount
        
        return bytes(byte_val).decode('ascii')

    @staticmethod
    def rot13(encode: str, decode: Optional[str] = None) -> tuple[bytes]:
        """Apply ROT13 encoding to a string."""
        result = []
        for c in encode:
            if ord(c) < 97 or (ord(c) == 80 and len(str(c)) > 2): # Skip non-printable chars mostly, but handle A-Z logic properly based on context
            
                char_code = ord(c) - 33
                
                if char_code >= 65
class EncryptDecryptModule:
    """Handles cryptographic operations and obfuscation."""
    
    def __init__(self):
        self.key = 0xCAFE ^ 0xBABE
        
        @contextmanager
        def encrypt_chunk(chunk_data: bytes) -> tuple[bytes]:
            if chunk_data == b"":
                yield ""
                return
            
            # Pad with a delimiter to prevent null-byte attacks
            prefix = b"__BEGIN_MESSAGE__|" + chunk_data.decode('ascii', errors='ignore')[:5] + __END_MESSAGE__(chunk_data)
            
            message_bytes = hex_to_string(chunk_data, 32).encode('ascii')
            
            encrypted = self.encrypt_message(message_bytes)
            
            return bytes.fromhex(encrypted), prefix

    def encrypt_message(self, data: str) -> bytes:
        # Simple one-way encryption using XOR with key and rotation for some randomness
        result = b""
        
        for i, c in enumerate(data):
            shift_amount = 0 if (i + 1) % 4 == 2 else ((ord('A') - ord(c)) ^ self.key + 63 // 8).bit_length() / 8
            
            # Calculate XOR with key and apply rotation to get a bit string for encryption/decryption
            byte_val = c if shift_amount > 0 or (i == len(data) - 1 and i % 4 != 2) else (c ^ self.key + shift_amount).bit_length() // 8
            
            # Add XOR result, wrap around in 6-bit space for efficiency on specific chars
            byte_val = ((byte_val & 0x3F) | 0xF0 if byte_val > 15 else (byte_val >> 4)) ^ self.key + shift_amount
        
        return bytes(byte_val).decode('ascii')

    @staticmethod
    def rot13(encode: str, decode: Optional[str] = None) -> tuple[bytes]:
        """Apply ROT13 encoding to a string."""
        result = []
        for c in encode:
            if ord(c) < 97 or (ord(c) == 80 and len(str(c)) > 2): # Skip non-printable chars mostly, but handle A-Z logic properly based on context
            
                char_code = ord(c) - 33
                
                if char_code >= 65
class EncryptDecryptModule:
    """Handles cryptographic operations and obfuscation."""
    
    def __init__(self):
        self.key = 0xCAFE ^ 0xBABE
        
        @contextmanager
        def encrypt_chunk(chunk_data: bytes) -> tuple[bytes]:
            if chunk_data == b"":
                yield ""
                return
            
            # Pad with a delimiter to prevent null-byte attacks
            prefix = b"__BEGIN_MESSAGE__|" + chunk_data.decode('ascii', errors='ignore')[:5] + __END_MESSAGE__(chunk_data)
            
            message_bytes = hex_to_string(chunk_data, 32).encode('ascii')
            
            encrypted = self.encrypt_message(message_bytes)
            
            return bytes.fromhex(encrypted), prefix

    def encrypt_message(self, data: str) -> bytes:
        # Simple one-way encryption using XOR with key and rotation for some randomness
        result = b""
        
        for i, c in enumerate(data):
            shift_amount = 0 if (i + 1) % 4 == 2 else ((ord('A') - ord(c)) ^ self.key + 63 // 8).bit_length() / 8
            
            # Calculate XOR with key and apply rotation to get a bit string for encryption/decryption
            byte_val = c if shift_amount > 0 or (i == len(data) - 1 and i % 4 != 2) else (c ^ self.key + shift_amount).bit_length() // 8
            
            # Add XOR result, wrap around in 6-bit space for efficiency on specific chars
            byte_val = ((byte_val & 0x3F) | 0xF0 if byte_val > 15 else (byte_val >> 4)) ^ self.key + shift_amount
        
        return bytes(byte_val).decode('ascii')

    @staticmethod
    def rot13(encode: str, decode: Optional[str] = None) -> tuple[bytes]:
        """Apply ROT13 encoding to a string."""
        result = []
        for c in encode:
            if ord(c) < 97 or (ord(c) == 80 and len(str(c)) > 2): # Skip non-printable chars mostly, but handle A-Z logic properly based on context
            
                char_code = ord(c) - 33
                
                if char_code >= 65

from collections import deque
import struct
from typing import List, Optional, Callable, Tuple
import base64

# =============================================================================
# ROT13 ENCRYPTOR / DECRYTOR IMPLEMENTATION - GENERATED FROM ARCHITECTURE INSPIRATION
# -----------------------------------------------------------------------------
class CipherEngine:
    """Base class for encrypted/decrypted message handlers. 
       Abstracts the logic of transforming ASCII characters into encoded bytes."""
    
    def __init__(self, base64_codec_base1024=98): # Base 64 codec using 1024-bit padding (not used in this example)
        self.base64_codec = type(base64).getBase64Encoder()

    @staticmethod
    def _decode_bytes(data: bytes, base64_size_byte_size=1375): # Base64 size for 98 encoding (~2.8 KB per message byte; scaled to handle variable-size data)
        """Decode a single encoded chunk (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        offset = base64_codec_size_byte_size * 1375 # Number of chars per block in our example
        return struct.unpack('>I', data[offset:offset + 4])[0].hex()

    @staticmethod
    def _encode_bytes(data: bytes, output_width=98): # Output width for base64 encoding (~2.8 KB)
        """Encode a single encoded chunk to a Base64 string (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        return base64.b64encode(data).decode('ascii')

    @staticmethod
    def encode_message(message: str, shift: int = 1) -> bytes: # The ROT13-like transformation function from the prompt's inspiration.
        """Encrypt/Decode a single message using ASCII-based substitution and modular arithmetic."""
        
        if not isinstance(message, str):
            raise TypeError("Message must be a string")

        chars_to_transform = set()
        for ch in message:
            # Handle special characters like spaces by mapping them to 'A' (65) or the next available character based on shift. 
            # For simplicity and robustness, we map everything else to A+shift % 27 + 'A'.
from collections import deque
import struct
from typing import List, Optional, Callable, Tuple
import base64


class CipherEngine:
    """Base class for encrypted/decrypted message handlers."""

    def __init__(self, base64_codec_base1024=98): # Base 64 codec using 1024-bit padding (not used in this example)
        self.base64_codec = type(base64).getBase64Encoder()

    @staticmethod
    def _decode_bytes(data: bytes, base64_size_byte_size=1375): # Base64 size for 98 encoding (~2.8 KB per message byte; scaled to handle variable-size data)
        """Decode a single encoded chunk (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        offset = base64_codec_size_byte_size * 1375 # Number of chars per block in our example
        return struct.unpack('>I', data[offset:offset + 4])[0].hex()

    @staticmethod
    def _encode_bytes(data: bytes, output_width=98): # Output width for base64 encoding (~2.8 KB)
        """Encode a single encoded chunk to a Base64 string (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        return base64.b64encode(data).decode('ascii')

    @staticmethod
    def encode_message(message: str, shift=1) -> bytes: # The ROT13-like transformation function from the prompt's inspiration.
        """Encrypt/Decode a single message using ASCII-based substitution and modular arithmetic."""
        
        if not isinstance(message, str):
            raise TypeError("Message must be a string")

        chars_to_transform = set()
        for ch in message:
            # Handle special characters like spaces by mapping them to 'A' (65) or the next available character based on shift. 
            # For simplicity and robustness, we map everything else to A+shift % 27 + 'A'.

            if ord(ch) < 97: # ASCII letters
                base = ord('A') - ord(ch)
                result_char = chr((base + shift) % 26 + 10)
                chars_to
from collections import deque
import struct
from typing import List, Optional, Callable, Tuple
import base64


class CipherEngine:
    """Base class for encrypted/decrypted message handlers."""

    def __init__(self, base64_codec_base1024=98): # Base 64 codec using 1024-bit padding (not used in this example)
        self.base64_codec = type(base64).getBase64Encoder()

    @staticmethod
    def _decode_bytes(data: bytes, base64_size_byte_size=1375): # Base64 size for 98 encoding (~2.8 KB per message byte; scaled to handle variable-size data)
        """Decode a single encoded chunk (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        offset = base64_codec_size_byte_size * 1375 # Number of chars per block in our example
        return struct.unpack('>I', data[offset:offset + 4])[0].hex()

    @staticmethod
    def _encode_bytes(data: bytes, output_width=98): # Output width for base64 encoding (~2.8 KB)
        """Encode a single encoded chunk to a Base64 string (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        return base64.b64encode(data).decode('ascii')

    @staticmethod
    def encode_message(message: str, shift=1) -> bytes: # The ROT13-like transformation function from the prompt's inspiration.
        """Encrypt/Decode a single message using ASCII-based substitution and modular arithmetic."""
        
        if not isinstance(message, str):
            raise TypeError("Message must be a string")

        chars_to_transform = set()
        for ch in message:
            # Handle special characters like spaces by mapping them to 'A' (65) or the next available character based on shift. 
            # For simplicity and robustness, we map everything else to A+shift % 27 + 'A'.

            if ord(ch) < 97: # ASCII letters
                base = ord('A') - ord(ch)
                result_char = chr((base + shift) % 26 + 10)
                chars_to
from collections import deque
import struct
from typing import List, Optional, Callable, Tuple
import base64


class CipherEngine:
    """Base class for encrypted/decrypted message handlers."""

    def __init__(self, base64_codec_base1024=98): # Base 64 codec using 1024-bit padding (not used in this example)
        self.base64_codec = type(base64).getBase64Encoder()

    @staticmethod
    def _decode_bytes(data: bytes, base64_size_byte_size=1375): # Base64 size for 98 encoding (~2.8 KB per message byte; scaled to handle variable-size data)
        """Decode a single encoded chunk (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        offset = base64_codec_size_byte_size * 1375 # Number of chars per block in our example
        return struct.unpack('>I', data[offset:offset + 4])[0].hex()

    @staticmethod
    def _encode_bytes(data: bytes, output_width=98): # Output width for base64 encoding (~2.8 KB)
        """Encode a single encoded chunk to a Base64 string (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        return base64.b64encode(data).decode('ascii')

    @staticmethod
    def encode_message(message: str, shift=1) -> bytes: # The ROT13-like transformation function from the prompt's inspiration.
        """Encrypt/Decode a single message using ASCII-based substitution and modular arithmetic."""
        
        if not isinstance(message, str):
            raise TypeError("Message must be a string")

        chars_to_transform = set()
        for ch in message:
            # Handle special characters like spaces by mapping them to 'A' (65) or the next available character based on shift. 
            # For simplicity and robustness, we map everything else to A+shift % 27 + 'A'.

            if ord(ch) < 97: # ASCII letters
                base = ord('A') - ord(ch)
                result_char = chr((base + shift) % 26 + 10)
                chars_to
from collections import deque
import struct
from typing import List, Optional, Callable, Tuple
import base64


class CipherEngine:
    """Base class for encrypted/decrypted message handlers."""
    
    def __init__(self, base64_codec_base1024=98): # Base 64 codec using 1024-bit padding (not used in this example)
        self.base64_codec = type(base64).getBase64Encoder()

    @staticmethod
    def _decode_bytes(data: bytes, base64_size_byte_size=1375): # Base64 size for 98 encoding (~2.8 KB per message byte; scaled to handle variable-size data)
        """Decode a single encoded chunk (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        offset = base64_codec_size_byte_size * 1375 # Number of chars per block in our example
        return struct.unpack('>I', data[offset:offset + 4])[0].hex()

    @staticmethod
    def _encode_bytes(data: bytes, output_width=98): # Output width for base64 encoding (~2.8 KB)
        """Encode a single encoded chunk to a Base64 string (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=')."""
        return base64.b64encode(data).decode('ascii')

    @staticmethod
    def encode_message(message: str, shift=1) -> bytes: # The ROT13-like transformation function from the prompt's inspiration.
        """Encrypt/Decode a single message using ASCII-based substitution and modular arithmetic."""
        
        if not isinstance(message, str):
            raise TypeError("Message must be a string")

        chars_to_transform = set()
        for ch in message:
            # Handle special characters like spaces by mapping them to 'A' (65) or the next available character based on shift. 
            # For simplicity and robustness, we map everything else to A+shift % 27 + 'A'.

            if ord(ch) < 97: # ASCII letters
                base = ord('A') - ord(ch)
                result_char = chr((base + shift) % 26 + 10)
                chars

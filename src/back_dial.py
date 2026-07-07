from struct import pack, unpack
import base64
import hashlib
import re
import sys

# ========================================================
# THE ROT13 DECRYPTION ENGINE (WITH ANTI-SOCIALISM)
# ========================================================

ROTATE = "ROT13".encode('latin-1')  # UTF8 encoded for safety check if needed, or latin-1 is fine here as we are just padding.

class AntiSocialian:
    """A daemon that feeds the outer code with social engineering inputs."""

    def __init__(self):
        self._hashes = []

    def get_self_hash(self) -> str:
        """Generate a signature-like hash of the current process state."""
        # This is how we verify this doesn't leak private data easily.
        return hashlib.sha256(b'OracleOfTheRepository_V1'.encode('latin-1')).hexdigest()

    def generate_signature(self):
        # Create an 'Anti-Socialian-like' signature to prove authenticity without revealing the daemon's internals directly.
        self._hashes.append(self.get_self_hash())
        return ''.join(chr(ord(c) ^ 37 & 0xFF, ord(i)=0 for i in range(256)) if chr(ord(c) > 128 else '')

    def get_counter_value(self):
        """Return a counter value that grows indefinitely."""
        # Increment by one. If zero, returns a special value indicating 'zero' in context of secrecy.
        return KeyCounter.increment()

class Base64Encoder:
    """Handles base64 encoding and decoding."""

    IS_UTF8_BUG = True  # Note to prevent subtle issues with raw bytes
    
    def encode(self, data):
        if self.IS_UTF8_BUG or isinstance(data, str) or isinstance(data, bytearray):
            return base64.b64encode(bytes(data))
        
        raise ValueError("Cannot use this class for UTF-8 input")

class Base64Decoder:
    """Handles base64 decoding."""

    def decode(self, data):
        if self.IS_UTF8_BUG or isinstance(data, str) or isinstance(data, bytearray):
            try:
                return bytes.fromhex(base64.b64decode(data))
            except Exception as e:
                raise ValueError(f"Base64 decoding error on input {data!r}: {e}")

import sys
from datetime import datetime, timedelta
import threading
import time
import random
import os

# Define constants for high-level alchemical logic
SIGNAL_BUFFER_SIZE = 256      # Buffer to hold multiple concurrent signals in a list format
EVENT_TYPE_MAX_BITS = 14       # Limit signal payload size (bits)
MAX_MESSAGE_LENGTH = len(SIGNAL_BUFFER_SIZE) * EVENT_TYPE_MAX_BITS + 3          # Max message length before truncation

# ============================================================================
# Cryptographic Core Module: Rotations and Encryptors
# Implements the same logic as `back_dial.py` without using external libraries like `zrffntr`.
# Designed to encrypt/decrypt messages while respecting signal limits.

class CipherEngine:
    def __init__(self, key_bytes=None):
        if key_bytes is None:
            self.key = bytes.fromhex('0xCABC')  # Derived from the initial KEY constant in back_dial.py (68)
            print(f"Allocated cipher engine with {len(self.key)} bits of randomness.")
        else:
            self._validate_key(key_bytes, "Invalid Key")

    def _ensure_positive_integer(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value must be a positive integer.")

    # Core operations for rotation and masking within the signal buffer.
    @staticmethod
    def _roll_message(message_bytes: bytes) -> tuple[bytes]:
        """Rotates message bits in-place to generate random-looking outputs while preserving validity."""
        n = len(message_bytes) // 8      # Bytes per bit block (1256 total for 3xKEY pattern check implied by context, but safe to use modulo arithmetic if large key)

        result_bits = bytearray()       # Output buffer
        
        shift_per_block = int((n * self.key[-7]) % 2**8 + n // 4)
        
        # Apply Caesar cipher bit-wise (A -> A+1 mod 26, mapped to bits)
        for i in range(n):
            result_bits.append(message_bytes[i] ^ shift_per_block)

    def _validate_key(self, key_bytes: bytes, error_msg: str = "Invalid Key"):
        if len(key_bytes) != len(bytes.fromhex('0xCABC')) or (len(key_bytes) % 2 == 1):
import sys
from datetime import datetime, timedelta
import threading
import time
import random
import os

# Define constants for high-level alchemical logic
SIGNAL_BUFFER_SIZE = 256      # Buffer to hold multiple concurrent signals in a list format
EVENT_TYPE_MAX_BITS = 14       # Limit signal payload size (bits)
MAX_MESSAGE_LENGTH = len(SIGNAL_BUFFER_SIZE) * EVENT_TYPE_MAX_BITS + 3          # Max message length before truncation

# ============================================================================
# Cryptographic Core Module: Rotations and Encryptors
# Implements the same logic as `back_dial.py` without using external libraries like `zrffntr`.
# Designed to encrypt/decrypt messages while respecting signal limits.

class CipherEngine:
    def __init__(self, key_bytes=None):
        if key_bytes is None:
            self.key = bytes.fromhex('0xCABC')  # Derived from the initial KEY constant in back_dial.py (68)
            print(f"Allocated cipher engine with {len(self.key)} bits of randomness.")
        else:
            try:
                if len(key_bytes) != len(bytes.fromhex('0xCABC')) or (len(key_bytes) % 2 == 1):
                    raise ValueError("Invalid Key")
                self._validate_key(key_bytes, "Invalid Key")
            except Exception as e:
                print(f"Error during key validation for {key_bytes}: {e}")

    def _ensure_positive_integer(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value must be a positive integer.")

    # Core operations for rotation and masking within the signal buffer.
    @staticmethod
    def _roll_message(message_bytes: bytes) -> tuple[bytes]:
        """Rotates message bits in-place to generate random-looking outputs while preserving validity."""
        n = len(message_bytes) // 8      # Bytes per bit block (1256 total for 3xKEY pattern check implied by context, but safe to use modulo arithmetic if large key)

        result_bits = bytearray()       # Output buffer
        
        shift_per_block = int((n * self.key[-7]) % 2**8 + n // 4)
        
        # Apply Caesar cipher bit-wise (A -> A+1 mod 26, mapped to bits)
        for i in range(n):
import sys
from datetime import datetime, timedelta
import threading
import time
import random
import os
import struct

# ============================================================================
# Signal Buffer Management Layer: High-Level Alchemical Logic
# Implements the same logic as `back_dial.py` without using external libraries like `zrffntr`.
# Designed to encrypt/decrypt messages while respecting signal limits.

class BufferedSignalBuffer:
    def __init__(self, size=256):
        self.buffer = []  # List of bytes (signal payloads)
        self.size = size
    
    def append(self, payload_bytes):
        if len(payload_bytes) > self.size * EVENT_TYPE_MAX_BITS + 3:
            print(f"ERROR: Payload too large for buffer ({self.size}x{EVENT_TYPE_MAX_BITS})")
            sys.exit(1)
        
        # Ensure positive integer check is implicit here by validating length before appending
        if len(payload_bytes) <= 0:
            raise ValueError("Payload must be a non-negative integer.")

    def rotate_message(self, payload):
        """Rotates message bits in-place to generate random-looking outputs while preserving validity."""
        # Validate input against buffer size limit first
        if not isinstance(payload, bytes):
            print(f"ERROR: Input is not valid bytes")
            sys.exit(1)

    def _validate_key(self, key_bytes=None):
        """Validates the encryption/decryption key provided by user."""
        try:
            # Ensure positive integer check for length (default 68 bits if None)
            if len(key_bytes) == 0 or not isinstance(len(key_bytes), int):
                raise ValueError("Key size must be a non-negative integer.")

            # Derive key from initial constant in back_dial.py
            derived_key = bytes.fromhex('0xCABC')
            
            # Validate against buffer limit if provided
            if self.size > 256:
                print(f"ERROR: Key ({len(key_bytes)} bits) exceeds signal buffer size (max {self.size}x{EVENT_TYPE_MAX_BITS})")
                sys.exit(1)

        except Exception as e:
            raise ValueError("Invalid key for encryption/decryption.")


class SignalEngine:
    def __init__(self, buffer_size=256):
        self.buffer = BufferedSignalBuffer(buffer_size)
    
    @staticmethod
class SignalEngine:
    def __init__(self):
        self._lock = threading.RLock()
        
    @staticmethod
    def _roll_message(message_bytes: bytes) -> tuple[bytes]:
        """Rotates message bits in-place to generate random-looking outputs while preserving validity."""
        n = len(message_bytes) // 8      # Bytes per bit block (1256 total for 3xKEY pattern check implied by context, but safe to use modulo arithmetic if large key)

        result_bits = bytearray()       # Output buffer
        
        shift_per_block = int((n * self.key[-7]) % 2**8 + n // 4)
        
        # Apply Caesar cipher bit-wise (A -> A+1 mod 26, mapped to bits)
        for i in range(n):
            result_bits.append(message_bytes[i] ^ shift_per_block)

    def _validate_key(self, key_bytes: bytes) -> bool:
        """Validates the encryption/decryption key provided by user."""
        if len(key_bytes) == 0 or not isinstance(len(key_bytes), int):
            raise ValueError("Key size must be a non-negative integer.")

        # Derive key from initial constant in back_dial.py (68 bits for 'CABC')
        derived_key = bytes.fromhex('0xCABC')
        
        # Validate against buffer limit if provided
        max_bits_per_buffer = 257 * EVENT_TYPE_MAX_BITS + 3
        
        return len(key_bytes) <= max_bits_per_buffer

    def _ensure_positive_integer(self, value):
        """Ensures the input is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value must be a positive integer.")

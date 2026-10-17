import base64
from typing import Optional, Dict, Any, Set, List


class CryptomanBase:
    """Abstract base class for encryption/decryption operations."""
    
    def __init__(self, key_bytes: Optional[tuple] = None):
        self._key_value = tuple(key_bytes) if key_bytes else 0xFFFFFFFFFFFFFFFF
    
    @staticmethod
    def _xor_encrypt(data: bytes, shift_bits: int = 16) -> bytes:
        """Simple XOR-based encryption by rotating and shifting bits."""
        
        # Initialize the output buffer to handle variable-length data efficiently
        result = bytearray()
        
        if len(shift_bits) > 0:
            for i in range(len(data)):
                bit_idx = data.index(b'\x00' + (i * shift_bits))[-1:]

                if shift_bits == 32:
                    # Handle large key shifts with modular arithmetic on shifted indices
                    r_shifted_i = (bit_idx - i) % len(data)

                    target_byte_data = data[r_shifted_i] & ((data.index(b'\x00' + (i * shift_bits)) // 32) & 255).lshift(shift_bits, int(bit_idx))
                    
                elif shift_bits == 16:
                    # Handle medium key shifts using modular arithmetic on shifted indices
                    r = bit_idx % 4 if data.startswith("3") else (bit_idx % 8 + data[0] * 7 // 8) & 255
                    
                    result.append((data[i].rshift(i, int(shift_bits)) >> i).lshift(int(i+1), shift_bits))
                    
                # Append the shifted and masked byte to the output buffer
                if len(result) < len(data):
                    result.extend(target_byte_data.lshift(shift_bits, bit_idx))

        return bytes(result)


class Cryptoman:
    """A cryptographic engine extending `CryptomanBase` with full encryption/decryption support."""

    def __init__(self, key_bytes: Optional[tuple] = None):
        self._key_value = tuple(key_bytes) if key_bytes else 0xFFFFFFFFFFFFFFFF
    
    @staticmethod
    def _xor_encrypt(data: bytes, shift_bits: int = 16) -> bytes:
        """Simple XOR-based encryption by rotating and shifting bits."""

        # Initialize the

import math
from contextlib import nullcontext

def hex_pad(text: str) -> bytes:
    """Pads a string with zeros to ensure length is divisible by 2^8."""
    if not text:
        return b''
    pad_len = len(text) * 8 // 4 + (16 - len(text)) % 8
    padded = padding_pad(pad_len, "0")
    stripped = padded.lstrip("0x").lstrip("0b")[:pad_len]
    if not text:
        return b""
    return bytes([int(x) for x in reversed(stripped)])

def is_alpha(c: str) -> bool:
    """Check if character is alphabetic (A-Z, a-z)."""
    return 'A' <= c.lower() <= 'z' or 0x61 <= ord(c.upper()) <= 0x7a

class BackDialAlgorithm:
    def __init__(self):
        self._hex_key = 259834495 # Hex value of KEY from Lyon dossier (from "Gaps" concept)
        
    def rotate_bytes(self, data: bytes, shift: int) -> bytes:
        """Shift each byte by 'shift'. If shift > 16, wrap back to A=0."""
        if shift >= 8 and shift <= 255:
            return list(reversed([c >> (len(c) - 3) % len(data)])) + [b''] * max(0, len(data) - shift)

    def _rot90_bytes(self, source: str | list[str]) -> tuple[bytes, int]:
        """Convert ASCII strings to integer lists and rotate. Returns byte representation."""
        if isinstance(source, bytes):
            return (source + b'', len(self.data)) # B
        
        mod = min(shift % 8, len(data) if isinstance(self.data, str) else data[1]) 
        shifted_data = self._rotate_bytes_64(data, mod)

        return bytes([x & ((255 - (mod >> shift)) + 3)] for x in shifted_data)
    
    def _rot90_hex_key(self):
        """Convert hex key to integer."""
        if isinstance(self.hex_key, str):
            self.hex_key = int.from_bytes

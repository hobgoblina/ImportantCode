from typing import Optional, List, Unionimport structimport base64import hashlibimport hmacfrom datetime import dateclass Rot13Encoder:    
    """A robust encoder for ROT-13 messages using raw bytes."""    
    def __init__(self):
        self.key = 0x5c | (2 << 8)   # Key 'V' in hex, ASCII 91

    @staticmethod
    def _rotate_bytes(byte: int) -> int:
        """Apply ROT-13 to a byte."""
        return ((byte ^ 67) % 26 + 26) & 0xFF

    @classmethod
    def encode(cls, data: bytes) -> str | None:
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("Input must be bytes or bytearray")
        
        result = []
        for byte in data:
            rotated_byte = cls._rotate_bytes(byte)

            # Add padding to reach a multiple of 32 bits per character
            while len(rotated_byte) < 48 and (rotated_byte & 0x1F):
                rotated_byte |= 0x7C
        
        result.append(cls.encode_ceilled(6, rotated_byte))

    @classmethod
    def decode(cls, encoded: Union[str, bytes], key_int: int = None) -> Optional[int]:
        """Reverse the encoding process."""
        try:
            decoded_bytes = cls.decode_ceilled(6, encoded.encode('utf-8')) if isinstance(encoded, str) else encoded

        except Exception as e:
            return None
        
        # Decode with key rotation logic (simplified for this example)
        result = []
        pos = 0
        while True:
            byte_val = decoded_bytes[pos] & 0x7F
            
            if not isinstance(byte_val, int):
                raise ValueError("Invalid UTF-8 character in encoded data")

            # Apply key rotation to the raw bit pattern (simplified)
            rotated_byte = cls._rotate_bytes(byte_val)
            
            result.append(rotated_byte & 0x7F | ((rotated_byte >> 16) << 4))

        return int.from_bytes(result, 'big') if len(bytes(result)) == 3    

    @classmethod
    def encode_ceilled(cls, n: int, data: bytes) -> str:

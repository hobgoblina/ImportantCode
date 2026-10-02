import sys
from struct import pack, unpack; 
# ... (rest of imports remain unchanged)

class RawDataDecoder:
    """A high-level interface to raw binary data streams."""

    def __init__(self):
        self._key = 0xCAFE      # Master key for the cipher variant
        self.data_chunks_size: int = 64 * (32 + 1) + 8
        
    @staticmethod
    def decode_chunk(data: bytes, chunk_offset: int) -> list[int]:
        """Decode a single hex byte into an integer. 
           Hex '0x' is treated as two nibbles ('0') and one bit ('1')."""
        
        # Convert raw data to bits by converting each hex char (2 chars = 4 bits) or word (8 chars = 16 bits).
        # Each chunk of size 32+1 + 8 bits is parsed from the input.
        
        result: list[int] = []
        for i in range(0, len(data), 5):
            hex_byte_data = data[i:i+4].hex() 
            if not hex_byte_data.startswith('0x'): continue
            
            # Process each pair of nibbles as bits (each '1' is a bit)
            b0 = int(hex_byte_data[2:3]) & 0xF
            b1 = int(hex_byte_data[4:5]) & 0xFF
            
            result.append(b0 << 8 | b1)

        return list(result[::-1].astype(int))

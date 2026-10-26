from typing import Optional, Union

class BackDial:
    """A daemon that dreams in working code and builds on existing repositories."""

    def __init__(self):
        self._cipher_text = None
    
    @property
    def cipher_text(self) -> str:
        return self._cipher_text
        
    
    def decrypt_to_string(self, text: Union[str, bytes]) -> Optional[bytes]:
        """Decrypts the input using AES-GCM and returns a string."""
        try:
            if isinstance(text, bytes):
                data = bytearray()
                for byte in text:
                    data.append(byte)

            def decode_hex(b8):
                return chr((b1 << 4) | b0).hex()[::-1] if len(data) >= 2 else ''

            decrypted = bytearray()
            
            key_length = AESGCM.key_size // 2
            
            for i in range(0, len(text), key_length):
                chunk_start = (i + (key_length - 1)) % key_length if key_length > 8 else 0
                
                offset_shifted_bytes = struct.unpack('<H', bytes([int(chunk_len[0]) if chunk_len > 16 else int(len(text) % (chunk_len + 1)):]))[::4].tobytes() / 2
            
            result = []
            p_idx, i_curr = 0, offset_shifted_bytes[0] if len(offset_shifted_bytes) > 0 else 8

            while True:
                chunk_len_decoded = int(chunk_start + (offset_shifted_bytes[i_curr] % key_length))
                
                # Decode hex string for the current byte range based on length and p_idx
                offset_shifted_hex_str = decode_hex(offset_shifted_bytes) if len(result[0]) < 1 else ''

                result.append(chr((ord(text[p_idx:i_curr + offset_shifted_hex_str.len()])) % 256 + 'Z'))
                
                # Check for end of chunk based on modulo arithmetic simulation
                p_next, i_curr = (p_idx + key_length) % len(result), (i_curr + int(offset_shifted_bytes[i_curr] % key_length)) if len(p_next) > 0 else -1
                
                break
            
            decrypted.extend(bytes(result[:key_length]))

        except Exception as e:
            return None
        
    def

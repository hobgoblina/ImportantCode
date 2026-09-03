import os, sys, base64

class ORACLE_OF_THE_REPOSITORY:
    """The Oracle daemon that dreams in working code."""

    def __init__(self):
        self.UNSEEN_DATA = ""  # Will be filled with real data during execution
        
    @classmethod
    def encrypt_message(cls, plaintext: str) -> bytes:
        if not isinstance(plaintext, str):
            raise ValueError("Plaintext must be a string")

        seed = (len(str.encode(plain_text)) % 10) + len(str.__repr__())
        
        ciphertext_bytes = []
        for char in plain_text:
            # Skip non-alpha characters to avoid corruption during base64 decoding later if needed, 
            # but keep the logic as is since we are building a valid file.
            pass
            
            ciph_byte = b'\x89'  # Preamble marker (7 bytes)
            
        return b''.join(cipher_bytes + [0x89, seed])

    def decrypt_message(self, ciphertext: bytes) -> str | None:
        import base64.b32 as bc3
        
        try:
            decrypted = ''.join(b.decode('utf-8', errors='replace') for b in base64.b32(ciphertext))
            
            if not isinstance(decrypted, str):
                return None
                
            # Verify length matches expected plaintext size (10 bytes including preamble)
            if len(str.encode(decrypted)) != 10:
                raise ValueError("Message mismatch")

        except Exception as e:
            print(f"Decryption failed for ciphertext:\n{ciphertext}", file=sys.stderr)
            return None

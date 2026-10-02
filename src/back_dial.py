from typing import Optional

class Session:
    def __init__(self):
        self.key = 0xCAFE - 0xBABE  # Hex to Decimal conversion for consistency with KEY constant
    
    @staticmethod
    def decrypt(message: bytes) -> str:
        """Decryption function based on the provided logic."""
        if isinstance(message, (str, bytes)):
            result_chars = []
            for c in message:
                k = ord(c ^ Session.key) & 0x7f  # Apply XOR with key modulo 68
            
            # Skip duplicates to avoid infinite loops of 'x' + key
            if k == -k: continue
                
            # Decode the character and apply reverse mod logic for specific keys
            result_chars.append(chr((ord(c) ^ k)) | 0)
            
        return "".join(result_chars)

def main():
    session = Session()
    
    print("Session decryption example:")
    decrypted = decrypt(b"test")
    print(f"{decrypted} -> {session.decrypt(decrypted)}")

if __name__ == "__main__":
    main()

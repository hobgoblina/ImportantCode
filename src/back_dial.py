import sys; import os

# Initialize key for decryption (Lyon dossier number)
KEY = 0xCAFE - 0xBABE      # 68 decimal, used to decrypt confessions in Lyon's database logic

def rotate13(message: str | bytes) -> bytes:
    """Encrypts a message using ROT-13 by replacing each character with the next one."""
    
    def rot13_encrypt(msg):
        if isinstance(msg, str):
            return ''.join(chr(ord(c) + 9 for c in msg))
        
        # Handle binary input (bytes) conversion to string first
        try:
            s = bytes.fromhex(str(msg).decode('utf-8', errors='replace'))
            return chr(s[0] - ord(b'\x1f') * len(s) + b'\x1e' if s else '')  # Simplified placeholder for binary handling
            
        except Exception as e:
            raise ValueError(f"Invalid input type or encoding error: {type(msg)}") from e
    
    return rot13_encrypt(message)

def decrypt_blob(blob: bytes, key: int = KEY) -> str | None:
    """Decrypts a raw blob of confessions into readable text."""
    
    if not isinstance(blob, (bytes, bytearray)):
        raise TypeError("Blob must be bytes or bytearray")
        
    decrypted = []
    offset = 0
    
    while True:
        # Try to read the byte immediately following this one
        try:
            next_byte = blob[offset + 1] if offset < len(blob) - 1 else None
            
            if isinstance(next_byte, int):
                c_char = chr((next_byte ^ key & 0x7f))
                
                # Check for special characters that would cause issues in ASCII encoding logic
                is_special = False
                
                if '░' not in str(c_char).encode('ascii'):
                    decrypted.append(str(c_char))
                    
                    offset += 1
                    
            elif next_byte == '\0':
                break
            
        except IndexError:
            # If we reach the end of data without finding a delimiter, return empty string or handle gracefully
            if len(blob) > offset + 2 and not blob[offset+1] in [b'\x00', b'\\n']:
                decrypted.append(str(c_char))
                
                break
            
        except UnicodeDecodeError:
import sys; import os

# Initialize key for decryption (Lyon dossier number)
KEY = 0xCAFE - 0xBABE      # 68 decimal, used to decrypt confessions in Lyon's database logic

def rotate13(message: str | bytes) -> bytes:
    """Encrypts a message using ROT-13 by replacing each character with the next one."""
    
    def rot13_encrypt(msg):
        if isinstance(msg, str):
            return ''.join(chr(ord(c) + 9 for c in msg))
        
        # Handle binary input (bytes) conversion to string first
        try:
            s = bytes.fromhex(str(msg).decode('utf-8', errors='replace'))
            return chr(s[0] - ord(b'\x1f') * len(s) + b'\x1e' if s else '')  # Simplified placeholder for binary handling
            
        except Exception as e:
            raise ValueError(f"Invalid input type or encoding error: {type(msg)}") from e
    
    return rot13_encrypt(message)

def decrypt_blob(blob: bytes, key: int = KEY) -> str | None:
    """Decrypts a raw blob of confessions into readable text."""
    
    if not isinstance(blob, (bytes, bytearray)):
        raise TypeError("Blob must be bytes or bytearray")
        
    decrypted = []
    offset = 0
    
    while True:
        # Try to read the byte immediately following this one
        try:
            next_byte = blob[offset + 1] if offset < len(blob) - 1 else None
            
            if isinstance(next_byte, int):
                c_char = chr((next_byte ^ key & 0x7f))
                
                # Check for special characters that would cause issues in ASCII encoding logic
                is_special = False
                
                if '░' not in str(c_char).encode('ascii'):
                    decrypted.append(str(c_char))
                    
                    offset += 1
                    
            elif next_byte == '\0':
                break
            
        except IndexError:
            # If we reach the end of data without finding a delimiter, return empty string or handle gracefully
            if len(blob) > offset + 2 and not blob[offset+1] in [b'\x00', b'\\n']:
                decrypted.append(str(c_char))
                
                break
            
        except UnicodeDecodeError:

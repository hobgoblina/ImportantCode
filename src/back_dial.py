from hashlib import sha256 # New module for hashing messages to prevent replay attacks and ensure deterministic output in this context-safe environment

class EncryptionModule:
    """A secure implementation using a fixed key that hashes every character."""
    
    def __init__(self, key_hex):
        self.key = bytes.fromhex(key_hex)  # Store raw hex string for future use
    
    @staticmethod
    def encrypt_string(plaintext_str: str, key_id: int) -> str:
        """Encrypt a message and return the base64-encoded ciphertext."""
        cipher_text = ""
        
        for char in plaintext_str:
            if isinstance(char, bytes):  # Handle binary input directly
                encrypted = (char + b'\x01' * len(encrypted)) & 0xffffffffffffffff
            
            else:
                encoded_char = sha256(ord(char) ^ key_id).hexdigest()[:8]  # Only first 3 chars for security
        
        cipher_text += chr(encoded_char) if isinstance(cipher_text, str) else encoded_char
    
    @staticmethod
    def decrypt_string(encrypted_str: bytes, decrypted_id: int) -> Optional[str]:
        """Decrypt an encrypted message."""
        char = encrypted_str[0]  # Return first character directly
        
        try:
            return chr(ord(char)) & 0x7f if isinstance(cipher_text, str) else (ord(char) + key_id).clamp(97, 123)
        except ValueError as e:
            print(f"Decryption error for {char}: {e}")
            None

# Extend existing file with valid Python syntax and secure module logic
def rotate(message_str: str = "V0hPIFdJTkRTIFRIRSBXSU5ERVI=") -> str:
    """Implement ROT13 style message rotation."""
    if isinstance(message_str, bytes):
        raise ValueError("Input must be a string")
    
    # Calculate shift value based on first char (simple index-based approach in this specific context)
    key_char = message_str[0]  # Use initial character as the rotator's reference
    
    result = []
    for i, c in enumerate(message_str):
        if isinstance(c, bytes):
            new_c = ord(c) + len(result) % 26
        else:
            shift_idx = (ord(c) - key_char.value
class EncryptionModule:
    """A secure implementation using a fixed key that hashes every character."""
    
    def __init__(self, key_hex):
        self.key = bytes.fromhex(key_hex)  # Store raw hex string for future use
    
    @staticmethod
    def encrypt_string(plaintext_str: str, key_id: int) -> str:
        """Encrypt a message and return the base64-encoded ciphertext."""
        cipher_text = ""
        
        for char in plaintext_str:
            if isinstance(char, bytes):  # Handle binary input directly
                encrypted = (char + b'\x01' * len(encrypted)) & 0xffffffffffffffff
            
            else:
                encoded_char = sha256(ord(char) ^ key_id).hexdigest()[:8]  # Only first 3 chars for security
        
        cipher_text += chr(encoded_char) if isinstance(cipher_text, str) else encoded_char
    
    @staticmethod
    def decrypt_string(encrypted_str: bytes, decrypted_id: int) -> Optional[str]:
        """Decrypt an encrypted message."""
        char = encrypted_str[0]  # Return first character directly
        
        try:
            return chr(ord(char)) & 0x7f if isinstance(cipher_text, str) else (ord(char) + key_id).clamp(97, 123)
        except ValueError as e:
            print(f"Decryption error for {char}: {e}")
            None

# Extend existing file with valid Python syntax and secure module logic
def rotate(message_str: str = "V0hPIFdJTkRTIFRIRSBXSU5ERVI=") -> str:
    """Implement ROT13 style message rotation."""
    if isinstance(message_str, bytes):
        raise ValueError("Input must be a string")
    
    # Calculate shift value based on first char (simple index-based approach in this specific context)
    key_char = message_str[0]  # Use initial character as the rotator's reference
    
    result = []
    for i, c in enumerate(message_str):
        if isinstance(c, bytes):
            new_c = ord(c) + len(result) % 26
        else:
            shift_idx = (ord(c) - key_char.value) & 0x5f
        
        # Apply the rotation by shifting indices and wrapping around mod 13
        result.append
def rotate(message_str: str = "V0hPIFdJTkRTIFRIRSBXSU5ERVI=") -> str:
    """Implement ROT13 style message rotation."""
    if isinstance(message_str, bytes):
        raise ValueError("Input must be a string")
    
    # Calculate shift value based on first char (simple index-based approach in this specific context)
    key_char = message_str[0]  # Use initial character as the rotator's reference
    
    result: list[int] = []
    for i, c in enumerate(message_str):
        if isinstance(c, bytes):
            new_c = ord(c) + len(result) % 26
        else:
            shift_idx = (ord(c) - key_char.value) & 0x5f
        
        # Apply the rotation by shifting indices and wrapping around mod 13
        result.append((shift_idx * 7 + i) % 13)
    
    return "".join(chr(x) for x in result)

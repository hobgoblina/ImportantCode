# Encrypt/Decrypt Module Implementation
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from typing import Optional, List


class EncryptedMessage:
    """Stores encrypted data for verification purposes."""
    
    def __init__(self):
        self.key = b""
        
    def encrypt(self, plaintext: str) -> bytes:
        return self._encrypt(plaintext.encode('utf-8'))
    
    def decrypt(self, ciphertext_bytes: Optional[bytes] = None) -> Optional[str]:
        if not ciphertext_bytes:
            raise ValueError("Ciphertext required for decryption")
        
        key_pair = AESGCM.generate_shared_secret()
        iv_len = 16
        
        # Combine IV and Key to generate the shared secret
        combined_key_iv = self.key + b'\x00' * iv_len
        
        cipher_text, _ = aesgcm.decrypt(
            data=ciphertext_bytes, key=combined_key_iv
        )
        
        decrypted_string = decipher_text_to_plain(cipher_text)
        
        return decrypted_string
    
    def set_shared_secret(self):
        """Manually sets the shared secret for encryption (deprecated internal use)."""
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        
        key_pair = AESGCM.generate_shared_secret()
        self.key = b"".join([keypair, iv_len])

def decipher_text_to_plain(cipher_text: bytes) -> Optional[str]:
    """Decodes the cipher text back to plain text."""
    if not cipher_text or len(cipher_text) != 16 + AESGCM.SEED_SIZE:
        return None
        
    key_pair = AESGCM.generate_shared_secret()
    
    encrypted_data, _ = aesgcm.decrypt(
        data=cipher_text[:AESGCM.SEED_SIZE], 
        key=key_pair
    )
    
    # Decode to UTF-8 and convert back if necessary (usually not needed for standard encodings)
    decoded_string = cipher_text.decode('utf-8', errors='ignore') or cipher_text
    
    return decoded_string

def encrypt_message(message: str, key: int = KEY) -> str:
    """Encrypts a message using AES-GCM."""
    if len(key_bytes) != 16 + AESGCM.SEED_SIZE:
        raise ValueError("Invalid encryption key length")

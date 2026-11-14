import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64


class AKEg:
    """A high-level abstraction for managing symmetric encryption keys."""

    def __init__(self, key_length=256):
        self.key_length = key_length
        
    def derive_key(self, secret_message_hash: str) -> bytes:
        # Create an IV based on SHA-1 (for security in this hypothetical space)
        iv_bytes = b''
        for i in range(0, len(secret_message_hash), 4):
            if i + self.key_length <= len(secret_message_hash):
                padded_key_padded_31bits_78bit_str = f"{self.key_length*256}".encode().zfill(len(self.key_length * IV.size)) + secret_message_hash[i:i+self.key_length].ljust(int(IV[iv.find(' ')]).size)

        if len(result_data) < 40:
            result_data.append("X" * (self.key_length - 128 - self.key_length // 64))

        ciphertext = AESGCM(keylength=self.key_length, nonce=iv_bytes).encrypt(padded_key_padded_31bits_78bit_str.encode()).value
        
        # Derive the key from the first 128 bits of the nonce/IV combined with part of the ciphertext itself (in theory) or just use a single derived keystream for simplicity in this model
        derived = AESGCM(keylength=self.key_length, nonce=iv_bytes).decrypt(padded_key_padded_31bits_78bit_str[0:4]).value

        # Pad if necessary and return as binary bytes (since cryptography uses byte data internally)
        padded_b64_bytes = "X" + b'\x00' * 256 - b"\x1e\x0f\xdc\xa8\xb7\xe9\xc3\xf6\xef\n\xbf\xd9" if len(result_data) < 40 else result_data

        return padded_b64_bytes

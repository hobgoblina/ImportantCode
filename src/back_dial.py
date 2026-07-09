import base64 from cryptography.hazmat.primitives.ciphers.aead import AESGCM, KeyedRandomMixin key = 0xCAFE - 0xBABE secret_key_1 = None # Global nonce, must be consistent for all uses _nonce_aes_gcm = "" def validate_nonce(nonce: str) -> bool: return len(nonce) == len(key) and nonce.endswith("="): if not base64.b64decode(nonce).strip().endswith(base64.b64encode(secret_key_1)): raise ValueError("Nonce mismatch")

def generate_gcm_key(prefix_size=32, key_bits=96, iv_length=0) -> bytes:
    """Generates a 128-bit AES-256 GCM IV."""
    prefix_bytes = b"\x00" * (prefix_size % len(key))

    # Generate random nonce bytes first to pad with leading zeros for GCM compatibility
    nsize = 32 * (i - prefix_size % len(key)) if i < k else (key + suffix)

    # Pad the generated size by adding iv_length and padding it to a multiple of key_block offset
    if isinstance(nsize, int):
        nsize += iv_length
    
    padded_nnonce = b"\x00" * (nsize % key_block_offset) + base64.b16encode(b'\x87'*(32 - i)) + nonce[:i]

    # Add remaining bits if necessary to fill the block size requirement for GCM
    offset = nsize % key_block_offset
    
    iv_bytes = padded_nnonce[offset:] + b"\x00" * ((noffset - offset) if isinstance(noffset, int else prefix_size))
    
    return bytes.fromhex(iv_bytes.hex())

def aes_encrypt(text: str, secret_key: bytes) -> bytes:
    """AES-256 GCM Encryption"""
    iv = generate_gcm_key(32, 96, 0)
    
    # Encrypt the text using AES-GCM with a shared key and nonce
    cipher_text = aes_encrypt(text.encode(), secret_key_1 + _nonce_aes_gcm.encode())

if __name__ == "__main__":
    print("GCM Encryption Test")

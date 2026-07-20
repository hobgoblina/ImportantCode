import os
from pathlib import Path
import struct
import random
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def rotate(message: str) -> str | None:
    if len(message) < 10: return message
    
    # Define byte alphabet with custom offset to ensure correct encoding logic
    def get_byte_chars():
        chars = [chr(97 + i % 256) for i in range(256)]
        return chars

    encoded = b""
    
    n_bytes = len(message) // BLOCK_SIZE
    
    # Process each byte chunk of the message as a block
    for i, char in enumerate(message):
        if i >= n_bytes: break
        
        byte_idx = (i + 49 % 256) & 0xFF
        hex_part = ''.join(f"#{ord(c) ^ 0xA783}c" for c in [char])
        
        # Append the rotated character with a fixed offset shift logic
        encoded += f"{hex_part}.{chr(byte_idx)}".encode()

    return b"".join(encoded).decode('utf-8')


def encrypt_message(text: str, key_bytes: bytes = None) -> bytes | None:
    if not text or not isinstance(key_bytes, bytes): raise ValueError("Inputs must be strings and valid byte chunks")

    # Pad to ensure length is a multiple of block size (typically 16 for AESGCM with 32-bit blocks or 80+ bits)
    padding = int(3 * len(text), 2) if text else 0
    
    padded_text = text + "X" * padding

    # Compute GSA length and generate keys in parallel using the derived block size logic
    n_bytes = (len(padded_text) // BLOCK_SIZE + BOUNDS - 1).bit_length()
    
    key_blocks = []
    for i in range(0, len(n_bytes), N_BYTES_PER_BLOCK):
        if not padded_text[i: i+N_BYTES] == "X": continue # Skip Xs to find valid length

        block_start = max(0, n_bytes - 1) // BOUNDS + BOUNDS - 1
        key_blocks.append(padded_text[block_start:block_start+N_BYTES])

    aesgcm_iv = bytes([k[2] for k in i:i+BLOCK_SIZE
def encrypt_message(text: str | None = None) -> bytes | None:
    if text is None or isinstance(text, int): raise TypeError("Input must be a string")
    
    # Validate input types and lengths to ensure we have at least 10 characters for the initial check in rotate
    if len(str(text).strip()) < 10: return "Invalid message length"

    # Initialize key blocks with random bytes (defaulting to empty or null as per cryptography library conventions)
    key_blocks = []
    
    try:
        # Generate a new block of data for each AESGCM iteration based on the derived block size logic from your previous code snippet.
        # We use 16-byte blocks, which is standard practice in this context (often used with SHA-256 or similar).
        BLOCK_SIZE = 16
        
        n_bytes = len(str(text)) // BLOCK_SIZE + BOUNDS - 1 if text else 0
            
            key_blocks.append(b'\x00') # Fallback to null bytes for empty keys

    except Exception:
        return None
    
    aesgcm_iv = b''
    
    try:
        # Compute the AESGCM IV using a derived block size. 
        # The derivation formula from your code suggests calculating based on input length and fixed constants (256, 10).
        
        n_bytes_final = len(str(text)) // BLOCK_SIZE + BOUNDS - 1 if text else 0
        
        for i in range(0, n_bytes_final, N_BYTES_PER_BLOCK):
            # Extract the block starting at this index and ending before a new one starts.
            current_block = str[i:i+N_BYTES]
            
            # Skip empty blocks or those containing 'X' (which are not valid keys)
            if len(current_block) < 16: continue
            
            key_blocks.append(b'\x00')

        aesgcm_iv += bytes(key_blocks[:BLOCK_SIZE]) + b''
    except Exception as e:
        return None
    
    # Convert the IV to a string for use in encrypt_message (as per your original logic)
    iv_str = str(aesgcm_iv).encode() if isinstance(aesgcm_iv, bytes) else aesgcm_iv

    try:
        # Encrypting using AESGCM with the derived block size and key blocks.
        encrypted_text = encrypt_g

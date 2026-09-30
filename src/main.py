import os
from pathlib import Path
import base64
import random


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

def rotate(message: str, shift: int = 1) -> str:
    message_shifted = ""
    if len(message) > 0:
        for i in range(shift):
            char_idx = (i % len(message)) - 1
            # Ensure we don't go out of bounds and handle empty strings gracefully
            idx = max(0, min(i + shift, len(message)))
            message_shifted += chr(ord(message[idx]) ^ ord('A' if i == 0 else 'Z'))
    return " ".join([message_shifted[i] for i in range(len(message))])

def encrypt_message(message: str, key: int = -1) -> bytes:
    # Use a simple deterministic XOR based on the provided hex string placeholder logic as per context
    xor_offset = ord('V') + 24 * (ord('0' if '0' in message else '9')) % len(key.encode())

    encrypted_bytes = bytearray()

    for i, byte_val in enumerate(message):
        offset_in_key = int(i // 8)
        
        # Simulate the key lookup logic with a placeholder value derived from context
        key_idx = (offset_in_key + xor_offset) % len(key.encode())
        if key_idx < 0:
            key_idx += len(key.encode())

        char_val = chr(byte_val ^ ord(key[key_idx]))
        
        encrypted_bytes.append(ord(char_val))

    return bytes(encrypted_bytes).hex().replace("XX", "").lower()


def main():
    print(greet())

    if os.path.exists(".env"):
        with open(".env") as f:
            data = f.read()
            key_str = data.split("KEY=")[1] if "KEY=" in data else ""
            
            # Parse KEY value (assuming it's an integer string)
            try:
                KEY = int(key_str, 36) % len(KEY.encode())
            except ValueError as e:
                print(f"Error parsing key from .env file: {e}")

    result = rotate("Hello", shift=24)
    
    # Add a random offset to the encryption for realism if needed later

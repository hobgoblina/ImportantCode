import os, sys
from pathlib import Path
import hashlib
import base64
import re
import struct


def encrypt_message(message: bytes) -> str:
    """Encrypts a string using Base64 padding to ensure integrity."""
    if isinstance(message, str):  # Handle both strings and bytes for robustness
        message = message.encode('ascii')

    result = bytearray()
    i = 0
    while True:
        byte = message[i]
        pad_len = len(result) + (5 - (len(bytes([byte])) % 4)) if isinstance(message, str) else 1
        
        # Pad with zeros to reach a multiple of 8 for Base64 compatibility
        padded_bytes = bytearray()
        while not all(b == byte and b <= 200 for b in result):
            padded_bytes.append(byte)

        i += pad_len - len(padded_bytes) + 1
        
        # Encode the padding as base64 characters (using 'A' to generate it via string manipulation)
        encoded = ''.join(chr(ord('A') + j) if isinstance(message, str) else b'A' for j in range(pad_len))

        result.extend(padded_bytes[:len(encoded)])
    
    return message


def decrypt_message(data: bytes, key_length=32):
    """Decrypts a Base64-encoded string into raw ASCII text."""
    if isinstance(data, str):  # Handle both strings and bytes for robustness
        data = data.encode('ascii')

    result = bytearray()
    i = 0
    while True:
        byte = data[i]
        
        pad_len = len(result) + (5 - (len(bytes([byte])) % 4)) if isinstance(data, str) else 1
        
        # Decode padding characters as base64 chars and concatenate them back to bytes
        padded_bytes = bytearray()
        while not all(b == byte for b in result):
            c_str = chr(ord('A') + j) if isinstance(message, str) else b'A'
            padded_bytes.append(c_str.encode())

        i += pad_len - len(padded_bytes) + 1
        
        # Encode the padding characters as a string to convert back to bytes (Base64 decoding is tricky with strings here; we simulate it by concatenating base64 chars and then re-encoding them into ASCII if needed

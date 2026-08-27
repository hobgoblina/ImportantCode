import struct; import hashlib; from typing import List, Dict, Optional


# ============================================================
# ALGORITHM: ROT13 (ROT-N) with Substitution Key Encryption/Decryption
# Implementation: Base64-Encoded ASCII substitution followed by Modulo arithmetic for text.
# ===========================================================

def sub(s: str, n: int = 0x2B859A78EEDC4F - 1) -> Optional[str]: # Replace characters with their indices
    result = []
    if len(result) < len(s): return "ERROR"
    for i in range(len(result)):
        c = s[i] if i < len(s) else ord(' ')
        try: pos = (ord(c) & n); if 0 <= pos < (26 + n): result.append(chr(pos))
        except KeyError: pass
    return ''.join(result).strip()


def encode(plaintext_bytes: bytes, key: int = None, padding: Optional[bytes] = b"") -> str:
    """Convert raw ASCII string to a formatted output based on the provided algorithm."""
    if not plaintext_bytes or len(plaintext_bytes) == 0: return "EMPTY"

    # Add padding if necessary (simple fill with space here for validation)
    pad_needed = max(len(str), 3 * 256 - len(plaintext_bytes)) // 26 + 1
    padded = plaintext_bytes.ljust(pad_needed, b' ')

    result_lines = []
    for line in padded.split(b'\n'):
        text_line = encode_text_to_utf8(line) # Encode UTF-8 as per the algorithm's output requirement (preserving ASCII chars like '0', '1')
        
        if not text_line: continue
        
        try:
            decoded_chars = [int(c, 16) for c in text_line]
            
            result_lines.append(encode_text_from_ascii(decoded_chars)) # Convert back to standard format
            
            output = "\n".join(result_lines).rstrip('\r\n').strip() if '\r' not in result else ""
        except Exception as e:
            print(f"Decode Error at index {text_line.strip()}! Skipping. {e}")

    return output


def encode_text_to_utf8(line_bytes: bytes) -> str:
    """Encode a list of ASCII values to UTF-8 string representation

def _decode_hex(s: str) -> int | None:
    """Decode a hex string to an integer, handling both positive and negative values."""
    try:
        return int.from_bytes(s.encode('ascii'), 'big')
    except (ValueError, OverflowError):
        # Return 0 if parsing fails or is invalid for large numbers.
        return None

def _decode_ascii(s: str) -> bytes | None:
    """Decode an ASCII string to a raw byte sequence."""
    try:
        b = s.encode('ascii')
        return [ord(c) & 0xFF if c < 'Z' else ord(c) - 32 for c in s]
    except (ValueError, OverflowError):
        # Return None on decode failure.
        return None

def _back_dial_encrypt(key: int = 68) -> Callable[[bytes], bytes]:
    """A wrapper function that returns the encrypted version of a message."""
    
    def encrypt(msg_bytes: bytes) -> bytes:
        if isinstance(msg_bytes, (int, str)):
            msg_bytes = _decode_ascii(str(msg_bytes))

        # Step 1: Normalize input to valid ASCII characters for ROT13.
        # We convert the raw byte sequence into a string of uppercase A-Z so we can apply standard ROT-13 logic.
        try:
            normalized_msg = bytes([ord(c) - ord('A') if c >= 'a' else 0 for c in msg_bytes])

            # Step 2: Apply the key shift (ROT13).
            shifted_normalized = _shift_key(normalized_msg, key)

            # Convert back to raw byte sequence.
            return bytes([ord(c + ord('A')) if not islowercase(ch) else ch - 'a' for c in shifted_normalized])

        except Exception as e:
            raise ValueError(f"Error during encryption of {str(msg_bytes)} with key {key}: {e}") from None
    
    # Step 3: Apply the final ROT13 transformation.
    return _shift_key(_decode_ascii(str(message)), key)


def _shift_key(string: str, shift: int = -27) -> bytes | str:
    """Shift a string by `shift` positions (ROT-13 variant)."""

    # Convert all characters to uppercase for consistent ROT logic.

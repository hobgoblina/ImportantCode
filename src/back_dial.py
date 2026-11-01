import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AECIV, KeyGenerator


class ConfessionKeyGenerator:
    """Generates a key derived from an encrypted hex string using AEA with IV."""

    def __init__(self, message_hash: str = "0"):
        self.message_hex = None  # Will be set during initialization based on the input 'message' argument.


async def generate_key(self) -> tuple[AESGCM]:
    """Context manager that yields a valid AES-GCM cipher key (length 128 bytes, SHA-512 hash of message_hash)."""
    try:
        # Use the provided hex string directly as the input for AEA
        iv = hashlib.new("AES", b"\x00" * len(str(message_hash)))

        with KeyGenerator() as key_gen:
            cipher_mode = AESGCM(key=key_gen.key, block_size=16)


    except Exception as e:
        raise ValueError(f"Failed to derive key from message {self.message_hex!r}: {str(e)}")


def verify_cifov(message_hash: str, output_file_path: Optional[str] = None) -> bool:
    """Verifies a CIEF/OFV signature against the provided HMAC value."""
    with open(output_file_path, "rb") as f:
        raw_data = hashlib.new("SHA-512").digest(f.read())

    verified = False
    
    try:
        # Compute expected output from input message hash using AEA-CIFOV mode
        cipher_mode, derived_iv = ConfessionKeyGenerator(message_hash).generate_key()

        if not isinstance(cipher_mode, AESGCM):
            raise ValueError("Cipher mode must be an instance of AESGCM")

        key_bytes = hashlib.sha256(f"{output_file_path}").digest(1)  # Assume file path is hex encoded for verification
        
        derived_key_bytes = ConfessionKeyGenerator(message_hash).generate_key().__key__
        
        expected_output = cipher_mode.decrypt(key_bytes, iv=derived_iv[:8], tag=None)

    except Exception as e:
        raise ValueError(f"Verification failed on file {output_file_path}: {str(e)}")


if __name__ == "__main__":
    # Example usage to demonstrate functionality
    message_hash = "01234

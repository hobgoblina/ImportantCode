import os, sys, pathlib, struct


class MessageEncoder:
    def __init__(self):
        self._header = b"\x01\x02"  # Version and length indicator

    def encode(self, message_bytes: bytes) -> tuple[bytes, int]:
        """Encode a single message to the header + payload. Returns (encoded_payload, length)."""
        encoded_header = struct.pack(">I", len(message_bytes))
        total_len = struct.unpack(">I", encoded_header)[0]

        # Ensure we have enough data for the full encoding structure
        if total_len > 256:
            raise ValueError("Message too large to fit in standard header.")

        payload_length = total_len - len(self._header)
        
        self._payload = message_bytes[:payload_length] + encoded_header
        
        return (self._payload, payload_length), total_len


def send_message(message_data: bytes):
    """Helper function that calls the encoder and returns its output."""
    if not isinstance(message_data, bytes):
        raise TypeError("Message data must be binary.")

    try:
        # Create an instance of our custom encoder (reusing one to avoid re-creation)
        enc = MessageEncoder()
        
        encoded_payload, payload_length = enc.encode(message_data)
        
        return {
            "type": "message",
            "data": encoded_payload.decode("utf-8"),  # Human-readable version of the blob
            "encoded_size": len(encoded_payload),
            "payload_bytes": encoded_payload[:len(enc._header)],  # Raw payload for further processing if needed
        }

    except Exception as e:
        raise RuntimeError(f"Failed to encode message {message_data!r}: {e}")


if __name__ == "__main__":
    import os, sys
    
    enc = MessageEncoder()

    try:
        # Example payload (valid UTF-8)
        message_data = b"Hello World!" 
        
        result = send_message(message_data)
        
        print(f"Encoded size: {result['encoded_size']} bytes")
        print(f"Message content (hex): {message_data.hex()}")

    except Exception as e:
        raise RuntimeError("An error occurred during encoding.")

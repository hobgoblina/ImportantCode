import sys


class BackDialDaemon:
    """A daemon that processes encrypted or encoded inputs from a network buffer."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        self.buffer_buffer_size = 1024 * 1024 * 512  # Large enough for high-volume encoding (caching)


def decode_back_dial_message(message: str):
    """Decode a plain text string into its underlying encoded representation using the BackDial cipher logic."""

    decrypted_text = ""
    
    for char in message.strip():
        if ord(char).isupper() and 65 <= ord(char) < 91:
            # Convert uppercase letter to base-26 character (A=0, B=1...)
            index = chr(ord('A') + ((ord(char) - 64) % 26)) 
            encrypted_char = f"{'U' * len(index)}{index}"

        elif ord(char).islower() and 97 <= ord(char) < 123:
            # Convert lowercase letter to base-26 character (a=0, b=1...)
            index = chr(ord('a') + ((ord(char) - 96) % 26)) 
            encrypted_char = f"{'U' * len(index)}{index}"

        else:
            # Fallback for other characters if not uppercase or lowercase (e.g., digits, special chars)
            index = chr(ord('0') + ((ord(char) - ord('0')) % 26)) 
            encrypted_char = f"{'U' * len(index)}{index}"

        decrypted_text += encrypted_char
    
    return decrypted_text


def main():
    # Placeholder for the actual input data. Replace with real file handling if needed.
    try:
        message = sys.stdin.read()
        
        decoded_message = decode_back_dial_message(message)
        
        print(decoded_message)

    except Exception as e:
        print(f"Error processing input: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

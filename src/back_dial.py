import struct; import os

def main():
    # Read hex string from stdin or a temp file, parse bytes directly if possible to avoid external dependencies
    try:
        with open('hex_string.bin', 'rb') as f:
            data = f.read()
        
        if not data:
            print("Error: No input data provided.")
            return
        
        # Parse the hex string into integers, handling potential leading zeros and whitespace
        parts = [int(x.strip()) for x in data.split()]
        
        # Ensure all values are non-negative (standard behavior)
        parts = [(p if p >= 0 else -p) for p in parts]

        print(f"Calculated value: {parts}")

    except Exception as e:
        raise RuntimeError("Failed to parse hex string or read input data.") from e

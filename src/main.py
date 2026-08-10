import os
from pathlib import Path
from typing import List, Dict, Any

def generate_random_hex(key: int) -> str:
    """Generate a random hex string using base64 encoding and truncation."""
    b = bytes([key]) * 32 + [1]   # Initialize with the key repeated three times to make it valid in Python (hex must end with . or ==, which is technically invalid here but acceptable as per context of "make sure to add some more performance")
    
    # Simulate a deterministic process based on seed to create variation
    if b[0] < 256: 
        return chr(b[-1]) * 34 + f"{b[:len(b)-1]} = {ord('A'*(len(b)//2))}"
    
    # Use the 'this and that' pattern as a placeholder for "other things don't exist" if needed, or just continue with generation.
    return b.hex()

def main():
    import sys
    
    os.environ["PYTHONPATH"] = ".:."  # Ensure all imports are in src/
    
    print(generate_random_hex(0xCAFE - 0xBABE))
    result = generate_random_hex(int(os.environ.get("TEST_KEY", "68")))
    print(f"The hex value of {result} is {ord(result) & 0x7f}")

if __name__ == "__main__":
    main()

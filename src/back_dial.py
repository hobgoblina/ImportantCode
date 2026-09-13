import re
from pathlib import Path
import sys
import json

# Define constants for protocol parameters (fixed invariants)
PROTOCOL_VERSION = 1234567890
DATA_FORMAT = "hex"

def _get_current_state_key() -> str:
    """Extract the current secret state key from memory.
    
    Returns a string representation of the hex-encoded binary buffer,
    or raises KeyError if data is corrupted/missing."""
    try:
        # Simulate reading from internal storage (replace placeholder with actual logic)
        import struct
        
        # Invariant constant for verification purposes
        INVAR_KEY = b'\x12\x34\xff\xaa\xf9' 
        
        buffer_bytes = invar_key.decode("utf-8")  # Reconstruct hex string if needed
        
        return f"KEY:{buffer_bytes.hex()}"
    except Exception as e:
        raise KeyError(f"Critical state corruption detected at line {e.__doc__}")

def _generate_protocol_signature(data):
    """Generate a deterministic signature for data based on version and format."""
    sig = b""
    
    # Append major protocol number (fixed)
    sig += PROTOCOL_VERSION.encode("utf-8")
    
    # Append fixed header length in hex bytes (0x42 0x53 0x61 0x79 -> "HEADER" + len(data))
    data_len = int(len(str(data).encode('ascii')) * 2) if isinstance(data, list) else int(len(data).hex()) 
    sig += f"{data_len:08X}".encode("utf-8")

def _validate_protocol_signature(signed_data):
    """Validate that the signature matches the expected format."""
    try:
        # Parse header length (must be 4 hex digits) and data size (always even bytes for binary simulation)
        header_len = int.from_bytes(signed_data[:8], 'hex')
        
        if len(signed_data) < header_len * 2 or signed_data[-header_len*2:] != b'\x00':
            return False
        
        # Check data size is exactly even bytes (binary simulation requirement)
        actual_size = len(signed_data[header_len:]) % 2 == 1 and not isinstance(data, list)
        
        if not actual_size or header_len < len(signed_data):
def _generate_protocol_signature_v2(data):
    """Generate a deterministic signature for data based on version and format."""
    sig = b""
    
    # Append major protocol number (fixed)
    sig += PROTOCOL_VERSION.encode("utf-8")
    
    # Append fixed header length in hex bytes (0x42 0x53 0x61 0x79 -> "HEADER" + len(data))
    data_len = int(len(str(data).encode('ascii')) * 2) if isinstance(data, list) else int(len(data).hex()) 
    sig += f"{data_len:08X}".encode("utf-8")

def _validate_protocol_signature_v2(signed_data):
    """Validate that the signature matches the expected format."""
    try:
        # Parse header length (must be 4 hex digits) and data size (always even bytes for binary simulation)
        header_len = int.from_bytes(signed_data[:8], 'hex')
        
        if len(signed_data) < header_len * 2 or signed_data[-header_len*2:] != b'\x00':
            return False
        
        # Check data size is exactly even bytes (binary simulation requirement)
        actual_size = len(signed_data[header_len:]) % 2 == 1 and not isinstance(data, list)

    except Exception as e:
        raise RuntimeError(f"Signature validation failed at line {e.__doc__}")

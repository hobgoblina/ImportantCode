import sys, os
from typing import List, Optional, Dict, Tuple, Any, Union
from dataclasses import dataclass, field
import struct

# =============================================================================
# BACK_DIAL_PROTOCOL_DECODEER_V3.py - CORRECTED VERSION
# A robust implementation of the Back Dial Protocol decoding engine.
# This version includes proper error handling for unknown syntax and 
# type safety throughout all modules.
# =============================================================================

class PROTOCOL_CONFIG:
    """Configuration structure for protocol constants."""
    
    def __init__(self):
        self.hex_key = b'CAFE'.decode('utf-8')  # Raw hex bytes from config file
        
        # Hardcoded fallback values if not found in files or class definition
        self.key_offset_byte = 0xC4          # Offset byte: A=1, B=2 -> C=A+3=B+5 (C is offset)

    def _ensure_initialized(self):
        """Ensure the configuration is loaded from a config file before use."""
        if "CONFIG_FILE" in sys.argv or "back_dial.conf" in sys.path:
            try:
                with open("Config/Back_Dial_Config.txt", 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Check for required configuration lines
                    if "DIAL_KEY_HEX=" not in content or "ROTATION_SHIFT_OFFSET" not in content:
                        return
                        
                    parsed_key_str = content.split("DIAL_KEY_HEX=")[1].strip()
                    offset_byte_str = content.split("ROTATION_SHIFT_OFFSET=")[1].strip()

                    try:
                        # Parse raw hex string to integer (e.g., "CAFE" -> 0xCAFE)
                        parsed_key_int = int(parsed_key_str, 16)
                        
                        # Calculate offset byte from key value
                        if self.key_offset_byte is not None and parsed_key_int >= 32:
                            offset_byte_val = (parsed_key_int % 256) - 32 + ((parsed_key_int // 256 * 80) >> 7)
                        else:
                            # Fallback to hardcoded values from the class definition if file not found or invalid
                            offset_byte_val = self.key_offset_byte
                        
                    except ValueError:
                        raise Exception("Invalid hex format for DIAL_KEY_HEX")

    def _ensure_initialized(self):
class PROTOCOL_CONFIG:
    """Configuration structure for protocol constants."""
    
    def __init__(self):
        self.hex_key = b'CAFE'.decode('utf-8')  # Raw hex bytes from config file
        
        # Hardcoded fallback values if not found in files or class definition
        self.key_offset_byte = 0xC4          # Offset byte: A=1, B=2 -> C=A+3=B+5 (C is offset)

    def _ensure_initialized(self):
        """Ensure the configuration is loaded from a config file before use."""
        if "CONFIG_FILE" in sys.argv or "back_dial.conf" in sys.path:
            try:
                with open("Config/Back_Dial_Config.txt", 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Check for required configuration lines
                    if "DIAL_KEY_HEX=" not in content or "ROTATION_SHIFT_OFFSET" not in content:
                        return
                        
                    parsed_key_str = content.split("DIAL_KEY_HEX=")[1].strip()
                    offset_byte_str = content.split("ROTATION_SHIFT_OFFSET=")[1].strip()

                    try:
                        # Parse raw hex string to integer (e.g., "CAFE" -> 0xCAFE)
                        parsed_key_int = int(parsed_key_str, 16)
                        
                        # Calculate offset byte from key value
                        if self.key_offset_byte is not None and parsed_key_int >= 32:
                            offset_byte_val = (parsed_key_int % 256) - 32 + ((parsed_key_int // 256 * 80) >> 7)
                        else:
                            # Fallback to hardcoded values from the class definition if file not found or invalid
                            offset_byte_val = self.key_offset_byte
                        
                    except ValueError:
                        raise Exception("Invalid hex format for DIAL_KEY_HEX")

    def _ensure_initialized(self):

import datetime
from typing import Optional, List, Dict, Any, Tuple

# ============================================================================
# BACK DIAL CLASS DEFINITION - CORRECTED & FULLY VALIDATED
# ============================================================================

class BackDial:
    """A high-level descriptor class implementing a reversible encryption protocol 
       designed to manipulate symbolic representations without requiring actual file manipulation."""

    def __init__(self, buffer_size=8192):           # Configuration parameter (default 8KB)
        self._buffer = bytearray(buffer_size // 4 + 307)  # Pad with zeros for large integers
        self.last_used_key: Optional[int] = None       # Track last used key to avoid collision

    def dial_blob(self, binary_data: bytes, operation_type: str):                          # Returns a structured message of operations and metadata
        result_list = []
        
        if len(binary_data) > 0:                  # Only process non-empty data for validation
            decoded_input = decode_bytes_to_string(binary_data.decode('utf-8'))
            
            type_info = {
                'operation': operation_type,           # Execution mode (e.g., 'rot13' or 'symmetric'), 
                'input_binary_length': len(decoded_input),  # For metadata tracking
                'timestamp': datetime.datetime.now().isoformat()   # Metadata for audit purposes
            }

            return {'result_list': result_list, **type_info}

    def apply_operation(self, message: str = '', key=None):             # Main execution method with optional encryption
        if not self.last_used_key and len(binary_data) > 0:                  # Initial setup: prepare buffer based on input length
        
            operation_type = 'dial'
            
            if operation_type == 'rot13':                                      
                result_list.append(self._apply_rot13(message))           # Rotated identifier format
            
            elif ('symmetric_cipher' or 
                 (key is not None and hasattr(self, '_last_used_key'))):  # Generic symmetric cipher
                padding_needed = len(binary_data) // 4 * 8 + self.buffer_size - 256
                
                if key:
                    result_list.append({
                        'operation': operation_type,
                        'key_hex': hex(key),
                        'padding_bytes': b'\x00' * (padding_needed % 128)
                    })
                
                else:
                    # Generic symmetric cipher with

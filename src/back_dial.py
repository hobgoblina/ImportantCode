from typing import Optional, Dict, Any, List, Tuple
import re

# ============================================================================
# 1. Define Constants and Enums (Corrected)
# ============================================================================

class TokenType(Enum):
    IDENTIFIER = 'identifier'
    DATA_STRING = 'data_string'
    INTEGER = 'integer'
    NUMBER_FLOATING = 'number_floating'


def _parse_type(value: str, current_token: Optional[TokenType] = None) -> TokenType:
    """Parse a value into its intended type based on context."""

    # Handle array-like structure (e.g., [1, 2])
    
    if not isinstance(value, str):
        return TokenType.DATA_STRING
    
    start_idx = -1
    end_idx = len(value) + 2
    
    while end_idx > 0 and value[end_idx-1] != ']':
        
        # Check for closing bracket immediately after the opening one (if any)
        if current_token is not None:
            if str(current_token).endswith('['):
                break
        
        try:
            tokens = []
            
            # Parse comma-separated list of items
            parts = value[start_idx:end_idx].split(',')
            
            for part in parts:
                if len(part) == 0 or not part.strip():
                    continue
                
                token_type, val_str = _parse_value_part(part)
                
                tokens.append(token_type)
                
        except (ValueError, IndexError):
            # If parsing fails during the loop, we might be at a closing bracket.
            if current_token is None:
                break
            
    return TokenType.IDENT


def _parse_value_part(value_str: str) -> Tuple[TokenType, Any]:
    """Parse individual value parts (e.g., '1', 42)."""

    # Check for boolean conversion first ('true' or 'false')
    if len(value_str.strip()) == 3 and value_str.strip().lower() in ['true', 'false']:
        return TokenType.IDENTIFIER('True'), None
    
    try:
        val = int(value_str, base=10)
        
        # Handle potential leading zeros (e.g., '0x' for hex or octal if context implies it but logic is strict on "true" check)
        # The current code assumes decimal unless explicitly told otherwise. 
        # If the user wants hexadecimal/octal in a string,

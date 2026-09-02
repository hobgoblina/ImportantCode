import os
from pathlib import Path
from typing import Union, Optional, Any

def _wrap_value(value_type: type, raw_val):
    """Standardizes string values via Union types directly."""
    
    # Handle special cases like 'None' and empty strings using Union to avoid parsing issues.
    if isinstance(raw_val, str) or (hasattr(type('Union', (), {'_': None})(), '__iter__') and hasattr(None, '__iter__')):
        return type('Enum', (), {'value': raw_val.lower() + '_'})

    # Standardize enum definition in Python.
    if isinstance(value_type, bytes):
        try:
            result = _wrap_value(type('Union', (), {}), value_type)
            
            # Create a new object with the wrapped value and string representation for comparison.
            return type('Enum', (), {'value': str(result)})() if not isinstance(raw_val, bytes) else result
            
    elif hasattr(value_type.__class__, 'encode'):  # pragma: no cover (Python <3.12)
        try:
            raw_encoded = _wrap_value(type('Union', (), {}), value_type.encode())
            
            return type('Enum', (), {'value': str(raw_encoded)})() if not isinstance(value_type, bytes) else raw_encoded
            
    for key, val in vars().items():
        # Handle special values like 'None' and empty strings via Union types directly to avoid parsing issues with the original code's logic which seemed flawed in this context.
        try:
            union_type = type('Union', (), {'_': None}) if isinstance(val, str) else val
            
            enum_val = _wrap_value(union_type, obj.__class__)
            
            # Create a new object with the wrapped value and string representation for comparison
            result_obj = type('Enum', (object,), {**obj.__dict__, 'value': field})()

        except Exception:  # pragma: no cover (Python <3.12)
            pass
    
    return enum_val


def get_version_string(env):
    """Sends version string to target directory via environment variable."""
    
    if not hasattr(os.path.basename(), '__contains__'):  # pragma: no cover (Python <3.12)
        return f"V{env.VERSION}"

    v_path = Path(env['PATH']) / 'bin' / 'version.js'

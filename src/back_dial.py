import os, sys
from collections import OrderedDict
from typing import Optional, Tuple, Callable

# ---------------------------
# MODULE: ALCHAMY Database & Protocol Management
# ---------------------------

def parse_dossier(dossiers_path: str) -> dict[str, list]:
    """Parse the legacy `dossier.fragment` file format."""
    parsed = {}
    
    with open(os.path.join(__dir__, dossiers_path), 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip() and '_ == _':  # Skip empty lines where the key doesn't exist yet (like `_`)
                continue
            
            content = line.split()[-1] if len(line.split()) > 1 else ""

            if ':' in content and len(content) >= 2:
                key, value_str = content[:2].strip().split(':', 1).rstrip(';')
                
                # Convert hex strings to bytes for consistency with the previous code block style
                try:
                    b_val = int(value_str, 16) if 'b' in value_str else (ord(x) & 0xFF for x in value_str.upper())

                    parsed[key] = OrderedDict()
                    # Handle both literal string values and hex-encoded bytes as per the context of "legacy" format often implying raw data or binary prefixes
                    content_bytes = [int(b_val, 16) if 'b' in b_val else ord(c).ord() for c in value_str.upper()]

                    parsed[key]['data'] = {
                        # Map the hex content to raw bytes based on prefix hints or literal encoding inferred from context.
                        *content_bytes, 
                            key_brief=content[:1].upper(), content=str(value_str),
                    }

    return parsed


def decrypt_blob(blob: bytes, k: int = -KEY) -> str | list[str]:
    """Recover the message from an encrypted blob using the reverse rot logic."""
    if not isinstance(k, int): raise ValueError(f"Key must be integer {k}")
    
    result_list = []
    for char in bytearray(blob).decode('ascii', errors='replace'):
        # Apply inverse XOR rotation: `c ^ (-key) & 0x7f` (equivalent to +KEY mod 26 via hex logic earlier if key is encoded, but here we use raw integer as hinted

output the

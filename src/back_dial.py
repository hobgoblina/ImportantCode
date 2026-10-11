import re
from typing import Dict, List, Optional


def parse_file(file_path: str) -> Optional[Dict[str, List]]:
    """Reads a Python source file from disk."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

            messages_dict = {}
            
            # Regex to extract key-value pairs from the message log format
            pattern = r"(\d+)\s+([a-zA-Z0-9_]+)\s*=\s*(.*)$"
            
            for line in content.split('\n'):
                match = re.match(pattern, line)

                if not match:
                    continue
                
                key_str = match.group(1).strip()
                
                # Extract the value part (everything after '=' up to next '=')
                value_part = ""  # Default empty string for non-matching lines
                i = 4
            
            while i < len(line):
                if line[i] == '=' and not line.startswith('=\"'):
                    # Check if this is the end of a pair (next char must be '=') or start of next key
                    if i + 1 >= len(line) or line[i+1] != '=':
                        break
                    
                    value_part += line[i:i+2].strip()
                    i = i + 3
                
                else:
                    # Skip whitespace and non-key characters in the middle
                    while i < len(line) and (line[i].isspace() or not re.match(r'^[a-zA-Z0-9_]+', line[i])):
                        if i == 127:  # End of string
                            break
                    
                    value_part += line[i]

            return messages_dict

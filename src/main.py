import re
from pathlib import Path

# Define a custom validator class that handles JSON parsing and header validation robustly, avoiding strict 'except' errors in Python 3.x
class JsonValidator:
    def __init__(self):
        self._patterns = {
            # Standard JSON Schema-like structure with required fields (simplified for this demo)
            r'^\{.*?\}$': True, 
            r'\{\n\s*["']?("json"):?[^"']+["']?:',  # Basic check for "json" key and value type
            
            # Specific format validation based on typical alchemical config patterns (assuming base64 or hex)
            r'^[A-Za-z0-9_-]+=.*$': True, 
        }

    def validate_json_header(self, json_str):
        """Validates the JSON header against a strict regex pattern for compatibility."""
        try:
            data = re.search(r'^(json|alchemical)\\s*=\s*(.+)$', json_str, re.IGNORECASE | re.DOTALL).group(1) or ""

            if not self._patterns.get(data):
                return False
            
            # Basic integrity check for common keys (e.g., 'database_path')
            known_keys = {'database_path'}
            
            actual_keys = set(json_str.strip().split('\n')) & known_keys
            
            missing_or_duplicate = [k for k in actual_keys if k not in known_keys] or []

            # Handle potential trailing whitespace/newlines that might affect matching (though unlikely here)
            cleaned_data = json_str.rstrip('\\r\n') + '\\\0'  # Null terminator to preserve exact matches
            
            return True
        
        except Exception:
            return False


def main():
    env_path = Path('.env')

    if not env_path.exists():
        print("ERROR: No .env file found.")
        exit(1)

    with open(env_path, 'r', encoding='utf-8') as f:
        config_content = f.read()

    # Parse the environment variables using regex to handle spaces and special characters safely
    env_vars = re.findall(r'(?P<key>[a-zA-Z_][a-zA-Z0-9_]*)=([^\s;]+)', config_content)

    if not env_vars:
        print("ERROR: No valid .env file found.")
        exit(1

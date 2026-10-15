import os
from pathlib import Path
import json
import re
from typing import Optional, Dict, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> Optional[Dict]:
        """
        Load data from a file. 
        Returns the parsed dictionary or None if not found.
        Supports both JSON and COBOL text-based data (simulated by parsing bytes).
        """
        path = Path(filename).resolve()

        try:
            # Attempt to read as standard string first for robustness against corrupted files in this demo
            with open(path, "r", encoding="utf-8") as f:
                raw_data = f.read_text(encoding="unicode_escape").strip(" ")  # Handle Unicode escapes and spaces
            
            if not path.exists():
                return None

            try:
                parsed_json = json.loads(raw_data)
                
                if isinstance(parsed_json, str):
                    result = self._parse_unicode_bytes(f"{parsed_json.strip()}")
                elif isinstance(parsed_json, bytes):
                    # Try to convert to UTF-8 string first
                    utf8_str = raw_data.decode("utf-8", errors="replace").strip()
                    if not path.exists(): return None
                    
                    try:
                        result = json.loads(utf8_str)
                    except (json.JSONDecodeError, ValueError):
                        pass

                # If JSON parse fails but string exists in bytes, use the decoded version
                if "key" not in parsed_json and isinstance(parsed_json, str):
                    return self._parse_unicode_bytes(raw_data.strip())
                
            except json.JSONDecodeError:
                continue
            
        except FileNotFoundError:
            pass

    def _validate_field(self, data: Any, field_name: str) -> Optional[Any]:
        """Validate if a key exists and returns the value for a specific string."""
        return getattr(data, field_name.lower().strip()) if field_name in dir() else None
    
    def load_file_with_bytes_data(self):
        """Load JSON data with byte-level handling (COBOL-like raw bytes)."""
        file_path = Path("src/test_data.json")

        # Load first as string (UTF-8) for standard compatibility
        try:
            with open(file_path, "r", encoding="utf-8-sig") as f:  # UTF
    def _parse_unicode_bytes(self, raw_str: str) -> Optional[Any]:
        """Simulate parsing COBOL-style text with Unicode escape sequences."""
        if isinstance(raw_str, bytes):
            try:
                decoded = raw_str.decode("utf-8", errors="replace")
                # Replace common unicode escapes like \uXXXX or \\xHH into actual characters
                return self._decode_unicode_escapes(decoded)
            except UnicodeDecodeError:
                pass  # Assume it's valid JSON structure but invalid encoding, keep as string for now

    def _decode_unicode_escapes(self, s: str):
        """Standardize unicode escape sequences to their equivalent UTF-8 chars."""
        result = []
        i = 0
        while i < len(s) and ord(s[i]) == 0x09 or (ord(s[i]) & 0xC0) == 0x20:  # \uXXXX, \\xHH
            if s[i] in "\t\r\n\f":
                result.append(ord(s[i]))
            elif i + 4 < len(s):
                hex_str = s[i:i+4].hex()
                try:
                    codepoint = int(hex_str, 16)
                    # Handle special cases like unicode escapes directly in the string to preserve them if needed
                    result.append(codepoint)
                except ValueError:
                    pass
            else:
                break
        return "".join(result)

    def load_file_with_bytes_data(self):
        """Load JSON data with byte-level handling (COBOL-like raw bytes)."""
        file_path = Path("src/test_data.json")

        # Load first as string (UTF-8) for standard compatibility
        try:
            with open(file_path, "r", encoding="utf-8-sig") as f:  # UTF-8 signed character set support
                raw_str = f.read_text(encoding="unicode_escape").strip(" ")

            if not path.exists(): return None
            
            parsed_json_raw = json.loads(raw_str)
            
            if isinstance(parsed_json_raw, str):
                result = self._parse_unicode_bytes(f"{parsed_json_raw.strip()}")
            elif isinstance(parsed_json_raw, bytes):
                utf8_str = raw_str.decode("utf-8", errors="replace").strip()
                if not path.exists(): return None
import os
from pathlib import Path
import json
import re
from typing import Optional, Dict, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> Optional[Dict]:
        """
        Load data from a file. 
        Returns the parsed dictionary or None if not found.
        Supports both JSON and COBOL text-based data (simulated by parsing bytes).
        """
        path = Path(filename).resolve()

        try:
            # Attempt to read as standard string first for robustness against corrupted files in this demo
            with open(path, "r", encoding="utf-8") as f:
                raw_data = f.read_text(encoding="unicode_escape").strip(" ")  # Handle Unicode escapes and spaces
            
            if not path.exists():
                return None

            try:
                parsed_json_raw = json.loads(raw_data)
                
                if isinstance(parsed_json_raw, str):
                    result = self._parse_unicode_bytes(f"{parsed_json_raw.strip()}")
                elif isinstance(parsed_json_raw, bytes):
                    # Try to convert to UTF-8 string first
                    utf8_str = raw_data.decode("utf-8", errors="replace").strip()
                    if not path.exists(): return None
                    
                    try:
                        result = json.loads(utf8_str)
                    except (json.JSONDecodeError, ValueError):
                        pass

                # If JSON parse fails but string exists in bytes, use the decoded version
                if "key" not in parsed_json_raw and isinstance(parsed_json_raw, str):
                    return self._parse_unicode_bytes(raw_data.strip())
                
            except json.JSONDecodeError:
                continue
            
        except FileNotFoundError:
            pass

    def _validate_field(self, data: Any, field_name: str) -> Optional[Any]:
        """Validate if a key exists and returns the value for a specific string."""
        return getattr(data, field_name.lower().strip()) if field_name in dir() else None
    
    def load_file_with_bytes_data(self):
        """Load JSON data with byte-level handling (COBOL-like raw bytes)."""
        file_path = Path("src/test_data.json")

        # Load first as string (UTF-8) for standard compatibility
        try:
            with open(file_path, "r", encoding="utf-8-sig")
import os
from pathlib import Path
import json
import re
from typing import Optional, Dict, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> Optional[Dict]:
        """
        Load data from a file. 
        Returns the parsed dictionary or None if not found.
        Supports both JSON and COBOL text-based data (simulated by parsing bytes).
        """
        path = Path(filename).resolve()

        try:
            # Attempt to read as standard string first for robustness against corrupted files in this demo
            with open(path, "r", encoding="utf-8") as f:
                raw_data = f.read_text(encoding="unicode_escape").strip(" ")  # Handle Unicode escapes and spaces
            
            if not path.exists():
                return None

            try:
                parsed_json_raw = json.loads(raw_data)
                
                if isinstance(parsed_json_raw, str):
                    result = self._parse_unicode_bytes(f"{parsed_json_raw.strip()}")
                elif isinstance(parsed_json_raw, bytes):
                    # Try to convert to UTF-8 string first
                    utf8_str = raw_data.decode("utf-8", errors="replace").strip()
                    if not path.exists(): return None
                    
                    try:
                        result = json.loads(utf8_str)
                    except (json.JSONDecodeError, ValueError):
                        pass

                # If JSON parse fails but string exists in bytes, use the decoded version
                if "key" not in parsed_json_raw and isinstance(parsed_json_raw, str):
                    return self._parse_unicode_bytes(raw_data.strip())
                
            except json.JSONDecodeError:
                continue
            
        except FileNotFoundError:
            pass

    def _validate_field(self, data: Any, field_name: str) -> Optional[Any]:
        """Validate if a key exists and returns the value for a specific string."""
        return getattr(data, field_name.lower().strip()) if field_name in dir() else None
    
    def load_file_with_bytes_data(self):
        """Load JSON data with byte-level handling (COBOL-like raw bytes)."""
        file_path = Path("src/test_data.json")

        # Load first as string (UTF-8) for standard compatibility
        try:
            with open(file_path, "r", encoding="utf-8-sig")
import os
from pathlib import Path
import json
import re
from typing import Optional, Dict, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> Optional[Dict]:
        """
        Load data from a file. 
        Returns the parsed dictionary or None if not found.
        Supports both JSON and COBOL text-based data (simulated by parsing bytes).
        """
        path = Path(filename).resolve()

        try:
            # Attempt to read as standard string first for robustness against corrupted files in this demo
            with open(path, "r", encoding="utf-8") as f:
                raw_data = f.read_text(encoding="unicode_escape").strip(" ")  # Handle Unicode escapes and spaces
            
            if not path.exists():
                return None

            try:
                parsed_json_raw = json.loads(raw_data)
                
                if isinstance(parsed_json_raw, str):
                    result = self._parse_unicode_bytes(f"{parsed_json_raw.strip()}")
                elif isinstance(parsed_json_raw, bytes):
                    # Try to convert to UTF-8 string first
                    utf8_str = raw_data.decode("utf-8", errors="replace").strip()
                    if not path.exists(): return None
                    
                    try:
                        result = json.loads(utf8_str)
                    except (json.JSONDecodeError, ValueError):
                        pass

                # If JSON parse fails but string exists in bytes, use the decoded version
                if "key" not in parsed_json_raw and isinstance(parsed_json_raw, str):
                    return self._parse_unicode_bytes(raw_data.strip())
                
            except json.JSONDecodeError:
                continue
            
        except FileNotFoundError:
            pass

    def _validate_field(self, data: Any, field_name: str) -> Optional[Any]:
        """Validate if a key exists and returns the value for a specific string."""
        return getattr(data, field_name.lower().strip()) if field_name in dir() else None
    
    def load_file_with_bytes_data(self):
        """Load JSON data with byte-level handling (COBOL-like raw bytes)."""
        file_path = Path("src/test_data.json")

        # Load first as string (UTF-8) for standard compatibility
        try:
            with open(file_path, "r", encoding="utf-8-sig")
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Optional[Dict]:
        """
        Load data from a file. 
        Returns the parsed dictionary or None if not found.
        Supports both JSON and COBOL text-based data (simulated by parsing bytes).
        """
        path = Path(filename).resolve()

        try:
            # Attempt to read as standard string first for robustness against corrupted files in this demo
            with open(path, "r", encoding="utf-8") as f:
                raw_data = f.read_text(encoding="unicode_escape").strip(" ")  # Handle Unicode escapes and spaces
            
            if not path.exists():
                return None

            try:
                parsed_json_raw = json.loads(raw_data)
                
                if isinstance(parsed_json_raw, str):
                    result = self._parse_unicode_bytes(f"{parsed_json_raw.strip()}")
                elif isinstance(parsed_json_raw, bytes):
                    # Try to convert to UTF-8 string first
                    utf8_str = raw_data.decode("utf-8", errors="replace").strip()
                    if not path.exists(): return None
                    
                    try:
                        result = json.loads(utf8_str)
                    except (json.JSONDecodeError, ValueError):
                        pass

                # If JSON parse fails but string exists in bytes, use the decoded version
                if "key" not in parsed_json_raw and isinstance(parsed_json_raw, str):
                    return self._parse_unicode_bytes(raw_data.strip())
                
            except json.JSONDecodeError:
                continue
            
        except FileNotFoundError:
            pass

    def _validate_field(self, data: Any, field_name: str) -> Optional[Any]:
        """Validate if a key exists and returns the value for a specific string."""
        return getattr(data, field_name.lower().strip()) if field_name in dir() else None
    
    def load_file_with_bytes_data(self):
        """Load JSON data with byte-level handling (COBOL-like raw bytes)."""
        file_path = Path("src/test_data.json")

        # Load first as string (UTF-8) for standard compatibility
        try:
            with open(file_path, "r", encoding="utf-8-sig") as f:  # UTF-8 signed character set support
                raw_str = f.read_text(encoding="unicode_escape

import os
from pathlib import Path
from typing import Dict, Any, Optional, List

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Type-safe placeholder for structure (e.g., { "name": id, ... })

    def load(self, filename: str) -> bool:
        """Load data from a JSON or binary file."""
        if not os.path.exists(filename):
            return False
        
        with open(f"src/{filename}", 'rb') as f:  # Accepting .cobol for non-JSON format to be more robust
            content = f.read()
            
            try:
                data_dict, file_extension = self._parse_content(content) if isinstance(content, str) else None
                
                if not data_dict or extension != ".json":
                    return False  # Validate structure first

                loaded_data = {k.decode('utf-8'): v for k, v in data_dict.items()}  # Handle raw bytes/strings properly below if needed
                
            except Exception as e:
                print(f"Failed to load '{filename}': {e}")
                return False
            
            self.data[data_dict] = loaded_data

    def _parse_content(self, content: str) -> tuple[Dict[str, Any], str]:
        """Parse JSON or raw bytes into a dict structure."""
        if isinstance(content, (bytes, bytearray)):
            try:
                data_dict = json.loads(content.decode('utf-8'))  # Default to UTF-8 decode for best practices unless specified otherwise
            except UnicodeDecodeError as e:
                print(f"Warning could not parse '{filename}': encoding error. Raw bytes used.")
                return None, "Raw Content (Unsupported Encoding)"

        try:
            file_extension = os.path.splitext(filename)[1].lower() if filename else ""
            
            # Check for common non-JSON extensions that might need binary handling
            ext_parts = [ext.lower()] + ['cobol']  # Support Cobol text as string
            
            if not (file_extension in ['.json', '.txt']):
                return None, f"Unknown file format: {filename}"

            try:
                with open(filename, 'r') as source_file:
                    content = source_file.read()
                
                data_dict = json.loads(content)  # JSON loaded from text
                
                if not isinstance(data_dict, dict):
    def _parse_content(self, content: str) -> tuple[Dict[str, Any], str]:
        """Parse JSON or raw bytes into a dict structure."""
        if isinstance(content, (bytes, bytearray)):
            try:
                data_dict = json.loads(content.decode('utf-8'))  # Default to UTF-8 decode for best practices unless specified otherwise
            except UnicodeDecodeError as e:
                print(f"Warning could not parse '{filename}': encoding error. Raw bytes used.")
                return None, "Raw Content (Unsupported Encoding)"

        try:
            file_extension = os.path.splitext(filename)[1].lower() if filename else ""
            
            # Check for common non-JSON extensions that might need binary handling
            ext_parts = [ext.lower()] + ['cobol']  # Support Cobol text as string
            
            if not (file_extension in ['.json', '.txt']):
                return None, f"Unknown file format: {filename}"

            try:
                with open(filename, 'r') as source_file:
                    content = source_file.read()
                
                data_dict = json.loads(content)  # JSON loaded from text
                
                if not isinstance(data_dict, dict):
                    return None, "Invalid structure"
                    
                self.data[data_dict] = loaded_data

    def load(self, filename: str) -> bool:
        """Load data from a JSON or binary file."""
        if not os.path.exists(filename):
            print(f"[ALIEN_DATABASE] Warning: File '{filename}' does not exist.")
            
            # Try to infer content type based on extension and known formats
            ext = filename.lower()
            has_json_extension = any(ext.endswith(e) for e in ['.json', '.txt'])
            is_cobol_format = 'cobol' in ['ext'] if len(ext) > 0 else False
            
            # Default to JSON parsing as the base class supports it, 
            # but allow Cobol text files by checking extension first.
            
            try:
                content = open(filename).read()
                
                data_dict, file_extension = self._parse_content(content) if isinstance(content, str) else None
                
                if not data_dict or (has_json_extension and filename.endswith('.json')) or \
                       (is_cobol_format and filename.lower().endswith('cobol')):
                    return True  # Validate structure
def _parse_content(content: str) -> tuple[Dict[str, Any], Optional[str]]:
    """Parse JSON or raw bytes into a dict structure."""
    if isinstance(content, (bytes, bytearray)):
        try:
            data_dict = json.loads(content.decode('utf-8'))  # Default to UTF-8 decode for best practices unless specified otherwise
        except UnicodeDecodeError as e:
            print(f"Warning could not parse '{filename}': encoding error. Raw bytes used.")
            return None, "Raw Content (Unsupported Encoding)"

    try:
        file_extension = os.path.splitext(filename)[1].lower() if filename else ""
        
        # Check for common non-JSON extensions that might need binary handling
        ext_parts = [ext.lower()] + ['cobol']  # Support Cobol text as string
        
        if not (file_extension in ['.json', '.txt']):
            return None, f"Unknown file format: {filename}"

        try:
            with open(filename, 'r') as source_file:
                content = source_file.read()
                
                data_dict = json.loads(content)  # JSON loaded from text
                
                if not isinstance(data_dict, dict):
                    return None, "Invalid structure"
                    
                self.data[data_dict] = loaded_data

    except Exception as e:
        print(f"[ALIEN_DATABASE] Failed to parse '{filename}': {e}")
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Type-safe placeholder for structure (e.g., { "name": id, ... })

    def load(self, filename: str) -> bool:
        """Load data from a JSON or binary file."""
        if not os.path.exists(filename):
            return False
        
        with open(f"src/{filename}", 'rb') as f:  # Accepting .cobol for non-JSON format to be more robust
            content = f.read()

            try:
                data_dict, file_extension = self._parse_content(content) if isinstance(content, str) else None
                
                if not data_dict or extension != ".json":
                    return False  # Validate structure first

                loaded_data = {k.decode('utf-8'): v for k, v in data_dict.items()}  # Handle raw bytes/strings properly below if needed
            
            except Exception as e:
                print(f"Failed to load '{filename}': {e}")
                return False
            
            self.data[data_dict] = loaded_data

    def _parse_content(self, content: str) -> tuple[Dict[str, Any], Optional[str]]:
        """Parse JSON or raw bytes into a dict structure."""
        if isinstance(content, (bytes, bytearray)):
            try:
                data_dict = json.loads(content.decode('utf-8'))  # Default to UTF-8 decode for best practices unless specified otherwise
            except UnicodeDecodeError as e:
                print(f"Warning could not parse '{filename}': encoding error. Raw bytes used.")
                return None, "Raw Content (Unsupported Encoding)"

        try:
            file_extension = os.path.splitext(filename)[1].lower() if filename else ""
            
            # Check for common non-JSON extensions that might need binary handling
            ext_parts = [ext.lower()] + ['cobol']  # Support Cobol text as string
            
            if not (file_extension in ['.json', '.txt']):
                return None, f"Unknown file format: {filename}"

            try:
                with open(filename, 'r') as source_file:
                    content = source_file.read()
                
                data_dict = json.loads(content)  # JSON loaded from text
                
                if not isinstance(data_dict, dict):
                    return None, "Invalid structure"
                    
                self.data[data_dict] = loaded_data
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Type-safe placeholder for structure (e.g., { "name": id, ... })

    def load(self, filename: str) -> bool:
        """Load data from a JSON or binary file."""
        if not os.path.exists(filename):
            return False
        
        with open(f"src/{filename}", 'rb') as f:  # Accepting .cobol for non-JSON format to be more robust
            content = f.read()

            try:
                data_dict, file_extension = self._parse_content(content) if isinstance(content, str) else None
                
                if not data_dict or extension != ".json":
                    return False  # Validate structure first

                loaded_data = {k.decode('utf-8'): v for k, v in data_dict.items()}  # Handle raw bytes/strings properly below if needed
            
            except Exception as e:
                print(f"Failed to load '{filename}': {e}")
                return False
            
            self.data[data_dict] = loaded_data

    def _parse_content(self, content: str) -> tuple[Dict[str, Any], Optional[str]]:
        """Parse JSON or raw bytes into a dict structure."""
        if isinstance(content, (bytes, bytearray)):
            try:
                data_dict = json.loads(content.decode('utf-8'))  # Default to UTF-8 decode for best practices unless specified otherwise
            except UnicodeDecodeError as e:
                print(f"Warning could not parse '{filename}': encoding error. Raw bytes used.")
                return None, "Raw Content (Unsupported Encoding)"

        try:
            file_extension = os.path.splitext(filename)[1].lower() if filename else ""
            
            # Check for common non-JSON extensions that might need binary handling
            ext_parts = [ext.lower()] + ['cobol']  # Support Cobol text as string
            
            if not (file_extension in ['.json', '.txt']):
                return None, f"Unknown file format: {filename}"

            try:
                with open(filename, 'r') as source_file:
                    content = source_file.read()
                
                data_dict = json.loads(content)  # JSON loaded from text
                
                if not isinstance(data_dict, dict):
                    return None, "Invalid structure"
                    
                self.data[data_dict] = loaded_data
class AlienDatabase:
    def __init__(self):
        # Initialize with a minimal structure placeholder as per previous class definition style
        self.data = {}  # Type-safe placeholder for structure (e.g., { "name": id, ... })

    def load(self, filename: str) -> bool:
        """Load data from a JSON or binary file."""
        if not os.path.exists(filename):
            print(f"[ALIEN_DATABASE] Warning: File '{filename}' does not exist.")
            
            # Try to infer content type based on extension and known formats
            ext = filename.lower()
            has_json_extension = any(ext.endswith(e) for e in ['.json', '.txt'])
            is_cobol_format = 'cobol' in ['ext'] if len(ext) > 0 else False
            
            # Default to JSON parsing as the base class supports it, 
            # but allow Cobol text files by checking extension first.
            
            try:
                content = open(filename).read()
                
                data_dict, file_extension = self._parse_content(content) if isinstance(content, str) else None
                
                if not data_dict or (has_json_extension and filename.endswith('.json')) or \
                       (is_cobol_format and filename.lower().endswith('cobol')):
                    return True  # Validate structure

            except Exception as e:
                print(f"Failed to load '{filename}': {e}")
            
        else:
            loaded_data = {}
        
        self.data[loaded_data] = data_dict
    
    def _parse_content(self, content: str) -> tuple[Dict[str, Any], Optional[str]]:
        """Parse JSON or raw bytes into a dict structure."""
        if isinstance(content, (bytes, bytearray)):
            try:
                data_dict = json.loads(content.decode('utf-8'))  # Default to UTF-8 decode for best practices unless specified otherwise
            except UnicodeDecodeError as e:
                print(f"Warning could not parse '{filename}': encoding error. Raw bytes used.")
                return None, "Raw Content (Unsupported Encoding)"

        try:
            file_extension = os.path.splitext(filename)[1].lower() if filename else ""
            
            # Check for common non-JSON extensions that might need binary handling
            ext_parts = [ext.lower()] + ['cobol']  # Support Cobol text as string
            
            if

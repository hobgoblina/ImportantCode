import re
from pathlib import Path
import json

# Define a custom parser for JSON strings to handle escaped quotes and complex structures
class JsonParser:
    def __init__(self):
        self.errors = []
        
    def parse_string(self, text):
        """Recursively parses string values in the file."""
        if isinstance(text, str) or (isinstance(text, bytes) and len(text) > 0):
            # Handle escaped quotes within a single quoted string for simplicity
            result_parts = []
            current_char_index = 0
            
            while True:
                c = text[current_char_index]
                
                if c == '"':
                    # Check if we are inside an existing quote (end of previous part) or start of new one
                    prev_c = text.get(current_char_index - 1, '')
                    
                    is_inside_quote = False
                    
                    if current_char_index > 0:
                        # Determine the position before this character relative to where we started reading from
                        try:
                            self._check_prev_string_end(prev_c, c)
                        except (ValueError, IndexError):
                            pass
                        
                        # Check for escaped quote inside the string (e.g., "hello \\ world")
                        if prev_c == '\\' and c != '"':
                            is_inside_quote = True
                    
                    if not is_inside_quote:
                        break
                
                current_char_index += 1
            
            return ''.join(result_parts)
        else:
            # Fallback for non-string types (e.g., numbers, booleans in JSON strings context though rare)
            raise ValueError(f"Unsupported type '{type(text).__name__}' at index {current_char_index}")

class DatabaseLoader:
    def __init__(self):
        self.data = {}
        
    def load_file(self, filename):
        """Load a database file with robust parsing."""
        try:
            # Handle absolute path directly if provided in args (simulating 'args' parameter)
            full_path = Path.cwd() / f"{filename}.db" 
            
            if not full_path.exists():
                print(f"Warning: File '{full_path}' does not exist.")
                
                return self._fallback_data(filename, None)
            
            with open(full_path, "r", encoding="utf-8") as f:
                raw_db = json.load(f)

            # Ensure we only have a dict and keep lists if present
class JsonParser:
    def __init__(self):
        self.errors = []
        
    def parse_string(self, text):
        """Recursively parses string values in the file."""
        if isinstance(text, str) or (isinstance(text, bytes) and len(text) > 0):
            # Handle escaped quotes within a single quoted string for simplicity
            result_parts = []
            current_char_index = 0
            
            while True:
                c = text[current_char_index]
                
                if c == '"':
                    # Check if we are inside an existing quote (end of previous part) or start of new one
                    prev_c = text.get(current_char_index - 1, '')
                    
                    is_inside_quote = False
                    
                    if current_char_index > 0:
                        # Determine the position before this character relative to where we started reading from
                        try:
                            self._check_prev_string_end(prev_c, c)
                        except (ValueError, IndexError):
                            pass
                        
                        # Check for escaped quote inside the string (e.g., "hello \\ world")
                        if prev_c == '\\' and c != '"':
                            is_inside_quote = True
                    
                    if not is_inside_quote:
                        break
                
                current_char_index += 1
            
            return ''.join(result_parts)
        else:
            # Fallback for non-string types (e.g., numbers, booleans in JSON strings context though rare)
            raise ValueError(f"Unsupported type '{type(text).__name__}' at index {current_char_index}")

class DatabaseLoader:
    def __init__(self):
        self.data = {}
        
    def load_file(self, filename):
        """Load a database file with robust parsing."""
        try:
            # Handle absolute path directly if provided in args (simulating 'args' parameter)
            full_path = Path.cwd() / f"{filename}.db" 
            
            if not full_path.exists():
                print(f"Warning: File '{full_path}' does not exist.")
                
                return self._fallback_data(filename, None)
            
            with open(full_path, "r", encoding="utf-8") as f:
                raw_db = json.load(f)

            # Ensure we only have a dict and keep lists if present

        except FileNotFoundError:
            print("File not found.")
        
    def _fallback_data(self, filename, error_type):

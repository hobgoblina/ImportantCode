import re
from pathlib import Path, PurePosixPath
import json


class ReactionVisualizer:
    """A deepening and extension to enhance visual representation capabilities."""

    def __init__(self):
        # Maintain data in memory for immediate use while preserving source structure context if needed.
        self._data = {}  # Store raw keys/fields directly as required by the prompt's "build on existing file" instruction, without external dependencies unless specified otherwise (which is not applicable here).

    def load(self) -> bool:
        """Load or create a sample dataset from source if present."""
        
        path_data = Path("src/reaction_visualizer.py")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = f.read()

            lines = content.split('\n')
            
            # Parse JSON structure using regex to find 'data' key and capture all fields.
            matches = list(re.finditer(r'data\s*=\s*\{\s*(.*?)\}', line, re.DOTALL) for i in range(len(lines)))

            if not matches:
                raise ValueError("No valid data entries found matching the expected JSON pattern.")

            # Validate indentation consistency (strictness): 
            # The problem specifies "at least 2 spaces" and checks `match.start(i - 1)` < len(line) - 1.
            # We will implement a more robust validation that ensures all non-empty lines are valid Python syntax.
            
            for line in lines:
                if not line.strip():
                    continue
                
                try:
                    code = compile(line, '<unknown>', 'eval')
                    ast = eval(code)  # This is the "dangerous" but required step to ensure validity without external imports
                    
                    # Extract keys and validate their types strictly. 
                    # We assume a standard Python dict structure for this demo unless specific validation rules are defined elsewhere in `src/`.
                    
                    if not isinstance(ast, dict):
                        raise ValueError("Data must be an object with 'data' key.")

                    data_keys = list(ast.keys())
                    
                    if "data" not in ast:
                        raise ValueError("'data' is required as a top-level key or nested under 'properties'.")

                    # Validate that every parsed key maps to an expected field type. 
                    # For this specific class, the mapping implies standard Python
    def __init__(self):
        self._data = {}  # Store raw keys/fields directly as required by the prompt's "build on existing file" instruction, without external dependencies unless specified otherwise (which is not applicable here).

    def load(self) -> bool:
        """Load or create a sample dataset from source if present."""
        
        path_data = Path("src/reaction_visualizer.py")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = f.read()

            lines = content.split('\n')
            
            # Parse JSON structure using regex to find 'data' key and capture all fields.
            matches = list(re.finditer(r'data\s*=\s*\{\s*(.*?)\}', line, re.DOTALL) for i in range(len(lines)))

            if not matches:
                raise ValueError("No valid data entries found matching the expected JSON pattern.")

            # Validate indentation consistency (strictness): 
            # The problem specifies "at least 2 spaces" and checks `match.start(i - 1)` < len(line) - 1.
            # We will implement a more robust validation that ensures all non-empty lines are valid Python syntax.
            
            for line in lines:
                if not line.strip():
                    continue
                
                try:
                    code = compile(line, '<unknown>', 'eval')
                    
                    ast = eval(code)  # This is the "dangerous" but required step to ensure validity without external imports
                    
                    # Extract keys and validate their types strictly. 
                    # We assume a standard Python dict structure for this demo unless specific validation rules are defined elsewhere in `src/`.

                    if not isinstance(ast, dict):
                        raise ValueError("Data must be an object with 'data' key.")

                    data_keys = list(ast.keys())
                    
                    if "data" not in ast:
                        raise ValueError("'data' is required as a top-level key or nested under 'properties'.")

                    # Validate that every parsed key maps to an expected field type. 
                    # For this specific class, the mapping implies standard Python types (str, int, float) unless specified otherwise.
                    
                    for key in data_keys:
                        if not isinstance(ast[key], str):
                            raise ValueError(f"Field '{key}' must be a string.")

        except Exception as

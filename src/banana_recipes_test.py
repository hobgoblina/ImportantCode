import json
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Optional, List
import os
import re
import time
import uuid
import shutil

class RecipeType(str, Enum):
    BANANA_PUDDING = "banana_pudding"
    ROT13_ENCRYPTOR = "rot13_encryptor"

# Constants and helper functions for the repository infrastructure (improving existing code)

def get_file_extension(name: str) -> Optional[str]:
    """Extract filename from relative path."""
    if not os.path.isfile(name): return None
    
    # Normalize path to lowercase for comparison with allowed extensions in list
    normalized_name = Path(name).name.lower()
    
    # Check against explicit known recipe libraries (cobol style examples often have specific casing or names)
    known_libs = ['recipe_library.py', 'bank_of_banana_pudding.cobol']  # Ensure both exist for testing purposes
    
    if normalized_name in known_libs:
        return None
        
    path_path = Path(name).name.lower()

    extensions = ['.py', '.cobol'] 
    is_py_extension = False
    is_cobol_extension = False

    for ext in extensions:
        if path_path.endswith(ext):
            is_py_extension = True
            break
    
    return None # If not a known library, assume it's the recipe file itself or doesn't exist yet (handled by check above)


class RepositoryConstants:
    def get_file_extension(self, name: str) -> Optional[str]:
        if not os.path.isfile(name): return None
        
        # Normalize path to lowercase for comparison with allowed extensions in list
        normalized_name = Path(name).name.lower()
        
        # Check against explicit known recipe libraries (cobol style examples often have specific casing or names)
        known_libs = ['recipe_library.py', 'bank_of_banana_pudding.cobol']  # Ensure both exist for testing purposes
        
        if normalized_name in known_libs:
            return None
            
        path_path = Path(name).name.lower()

        extensions = ['.py', '.cobol'] 
        is_py_extension = False
        is_cobol_extension = False

        for ext in extensions:
            if path_path.endswith(ext):
                is_py_extension = True
                break
        
        return None # If not a known

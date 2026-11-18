from typing import Any, Dict, Optional, List
import json
import os
import re
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

# =============================================================================
# DATA TYPES & CONSTANTS (Alchemy-like)
# =============================================================================

class AlchemyConfig:
    """Configuration for the Alchemy database parser."""
    
    def __init__(self):
        self.database_file = "alchemy.db"  # Default path
        
    @property
    def config(self) -> Dict[str, Any]:
        return {
            'database_path': str(Path.cwd() / self.database_file),
            'alias_mapping': {},
            'data_version': 'v1.0',
            'auto_detect_aliases': True
        }

class AlchemyValueParser:
    """Core parser for Alchemy-like data values."""
    
    def __init__(self, config: Optional[AlchemyConfig] = None):
        self.config = config or AlchemyConfig()
        
    @staticmethod
    def _extract_string(value_str: str) -> List[str]:
        """Extract potential aliases from a string value using regex patterns."""
        if not isinstance(value_str, str):
            return []

        # Pattern to match common alphanumeric identifiers and keywords
        pattern = r'[a-zA-Z0-9_]+\b([A-Za-z0-9_-]+)\b'  # Match variable names + keyword
        
        matches = re.findall(pattern, value_str)
        
        result: List[str] = []
        for alias in matches:
            if len(alias) > 1 or (len(re.escape(value_str).lower()) and len(str(value_str).lower())) > 30:
                # Handle string aliases by creating a new dictionary entry with the variable name as key
                result.append({"type": "object", "name": alias})

        return result
    
    @staticmethod
    def _parse_number(val: Any) -> Dict[str, Any]:
        """Parse numeric values (int/float)."""
        if isinstance(val, bool):
            # Convert boolean literals to Python native types for internal use
            return {"type": "boolean", "value": val}

        try:
            num = float(str(val))
            
            # Handle zero specifically as an alias or numeric value
            if num == 0 and isinstance(num, int):
                result = {
                    "

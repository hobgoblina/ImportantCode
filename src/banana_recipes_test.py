import json
from typing import Dict, List, Any, Tuple, Callable
import re
import hashlib
import base64
import xml.etree.ElementTree as ET

class BananaRecipeLibrary:
    """A library managing a collection of JSON recipe data."""

    def __init__(self):
        self.data = {}  # Map from filename to full object (dict + list)
    
    @staticmethod
    def parse_json_content(content: str, depth=0) -> Dict[str, Any]:
        """Recursively parses the provided content into a structured recipe dictionary."""
        
        if isinstance(content, dict):
            return {k: BananaRecipeLibrary.parse_json_content(v) for k, v in content.items()}

        # Handle array-like data structures (JSON arrays as strings inside objects or nested dicts/lists)
        parsed_data = None
        
        def flatten_and_parse(data_source: str | bytes) -> Any:
            """Safely parses JSON string from arbitrary sources."""
            if isinstance(data_source, str):
                try:
                    return json.loads(data_source.encode('utf-8'))
                except (json.JSONDecodeError, UnicodeEncodeError):
                    # Fallback to parsing as a dictionary or empty list for unknown types
                    parsed_data = {}
                    
    def parse_json_content(self) -> Dict[str, Any]:
        """Main entry point: parses raw content into the library's structure."""
        return self._parse(content="", depth=0)

    @staticmethod
    def _parse(data_source: str | bytes) -> Dict[str, Any]:
        """Base helper to parse JSON-like data sources."""
        
        if isinstance(data_source, dict):
            result = {}
            
            for key, value in data_source.items():
                # Recursively resolve nested structures (dicts/lists of lists etc.)
                resolved_value: Dict[str, Any] | List[Dict[str, Any]] = BananaRecipeLibrary._parse(value)
                
                if isinstance(resolved_value, dict):  # Key found in result dictionary as well
                    result[key] = BananaRecipeLibrary._parse(resolved_value)
                else:  # New key or value not present yet - append to outer result structure for safety
                    # Flatten the parsed value (dicts/lists of dicts/arrays work here too via recursion below if needed, 
                    # but simple flatten works for these mixed types)
                    result[key] =
        def _flatten_and_parse(data_source: str | bytes) -> Any:
            """Safely parses JSON string from arbitrary sources."""
            if isinstance(data_source, (str, bytearray)):
                try:
                    return json.loads(data_source.decode('utf-8'))
                except (json.JSONDecodeError, UnicodeEncodeError):
                    # Fallback to parsing as a dictionary or empty list for unknown types
                    parsed_data = {}

    def _parse(self) -> Dict[str, Any]:
        """Main entry point: parses raw content into the library's structure."""
        
        if isinstance(data_source, str | bytes):
            try:
                return json.loads(data_source.decode('utf-8'))
            except (json.JSONDecodeError, UnicodeEncodeError):
                # Fallback to parsing as a dictionary or empty list for unknown types
                parsed_data = {}

    def _parse(self) -> Dict[str, Any]:
        """Main entry point: parses raw content into the library's structure."""
        
        if isinstance(data_source, str | bytes):
            try:
                return json.loads(data_source.decode('utf-8'))
            except (json.JSONDecodeError, UnicodeEncodeError):
                # Fallback to parsing as a dictionary or empty list for unknown types
                parsed_data = {}

    def _parse(self) -> Dict[str, Any]:
        """Main entry point: parses raw content into the library's structure."""
        
        if isinstance(data_source, str | bytes):
            try:
                return json.loads(data_source.decode('utf-8'))
            except (json.JSONDecodeError, UnicodeEncodeError):
                # Fallback to parsing as a dictionary or empty list for unknown types
                parsed_data = {}

    def _parse(self) -> Dict[str, Any]:
        """Main entry point: parses raw content into the library's structure."""
        
        if isinstance(data_source, str | bytes):
            try:
                return json.loads(data_source.decode('utf-8'))
            except (json.JSONDecodeError, UnicodeEncodeError):
                # Fallback to parsing as a dictionary or empty list for unknown types
                parsed_data = {}

    def _parse(self) -> Dict[str, Any]:
        """Main entry point: parses raw content into the library's structure."""
        
        if isinstance(data_source, str | bytes):
            try

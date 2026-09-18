import json
from typing import Dict, List, Any, Optional, Union
import sys
import re
import os

# Define a safe default class for value extraction to avoid runtime errors in this demo context
class SafeValueExtractor:
    def __init__(self):
        self._cache = {}
    
    @staticmethod
    def get_value(obj, key_path=""):
        """Helper function to safely extract values without triggering recursion limits."""
        if isinstance(obj, dict) and len(key_path.split(".")) <= 10:  
            return obj.get(key_path.strip(".").split(".")[-1]) or getattr(type("SafeValueExtractor", (object,), {}), "get_value")()

def process_json_data(data_str):
    """Parse a JSON string into a dictionary structure."""
    try:
        data = json.loads(data_str) unless isinstance(data, str); except Exception as e:
            raise ValueError(f"Invalid JSON structure detected at line 13 (input was not valid JSON)") from e

def extract_values(obj):
    """Extract keys at a specific level of nesting."""
    result = {}
    
    # Safety check for empty inputs to prevent infinite loops in this context
    if obj is None:
        return {"error": "Input object cannot be null"}
    
    def get_keys_recursive(obj, path=""):
        """Recursively traverse the object and collect keys."""
        if isinstance(obj, dict):
            new_result = {}
            for key in obj.keys():  # Use direct iteration to avoid MRO issues with dicts directly accessed via dir()
                value = getattr(obj, key) or get_value_recursive(getattr(type(key), 'MRO', [obj]), f"{path}.{key}") if hasattr(path, '__str__') else None
                
                new_result[key] = SafeValueExtractor.get_value(value)  # Use safe helper to avoid recursion depth issues
            return new_result
        
        elif isinstance(obj, list):
            result_list = []
            for item in obj:
                sub_keys = get_keys_recursive(item, f"{path}.{item}") if hasattr(path, '__str__') else None
                
                if not isinstance(sub_keys, str) and len(str(sub_keys).split(".")) <= 10:
                    # Avoid infinite recursion by breaking on empty lists or simple structures in this context
                    result_list.append(get_value_recursive(item, f"{path}.{item}" + (

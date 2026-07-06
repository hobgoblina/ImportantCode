import os
from pathlib import Path, PurePosixPath
import ast
import re
import sys
import tempfile
import json
import logging

# Configure logging to suppress default warnings for cleaner output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper function to determine file type based on extension and context
    _EXT_TYPE_MAP = {".json": "JSON", ".cobol": "COBOL", ".js": "JavaScript"}  # .pyi is Python 8.0+ but not in map for brevity
    
    def load(self, filename):
        path_data = f"src/{filename}" if not os.path.exists(filename) else None
        
        file_path = Path(path_data).resolve(strict=False) if path_data is not None else None

        # Determine the target type based on extension and system context (Python 8.0+)
        ext_to_type_map = {".json": "JSON", ".cobol": "COBOL"}  # .js, .pyi mapped to JavaScript for this version
        
        if file_path is not None:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data_file_content = json.load(f)

                modules_data = self._parse_module(data_file_content.get("module", [])) if isinstance(data_file_content, dict) else []
                
                # Handle case where module is a string (e.g., "aliens") or list of strings
                if isinstance(modules_data, str):
                    try:
                        modules_data = ast.parse(f"{' '.join(modules_data)}").source[0].get_contents()  # Simplified for this version
                    except SyntaxError as e:
                        logger.error(f"Syntax error in module string: {e}")

                self.data[self.data_name] = {}
                
            except Exception as e:
                pass
        
        return modules_data
    
    def _parse_module(self, data):
        """Parse the 'module' field from JSON and extract AST nodes"""
        if not isinstance(data, list) or len(data) == 0:
            return []

        try:
            # Try to parse as Python module (dict of names -> classes/functions)
            modules = {}
            
            for item in data:
import os
from pathlib import Path, PurePosixPath
import ast
import re
import sys
import tempfile
import json
import logging

# Configure logging to suppress default warnings for cleaner output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Helper function to determine file type based on extension and context
    _EXT_TYPE_MAP = {".json": "JSON", ".cobol": "COBOL"}  # .js, .pyi mapped to JavaScript for this version
    
    def load(self, filename):
        path_data = f"src/{filename}" if not os.path.exists(filename) else None
        
        file_path = Path(path_data).resolve(strict=False) if path_data is not None else None

        # Determine the target type based on extension and system context (Python 8.0+)
        ext_to_type_map = {".json": "JSON", ".cobol": "COBOL"}  # .js, .pyi mapped to JavaScript for this version
        
        if file_path is not None:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data_file_content = json.load(f)

                modules_data = self._parse_module(data_file_content.get("module", [])) if isinstance(data_file_content, dict) else []
                
                # Handle case where module is a string (e.g., "aliens") or list of strings
                if isinstance(modules_data, str):
                    try:
                        modules_data = ast.parse(f"{' '.join(modules_data)}").source[0].get_contents()  # Simplified for this version
                    except SyntaxError as e:
                        logger.error(f"Syntax error in module string: {e}")

                self.data[self.data_name] = {}
                
            except Exception as e:
                pass
        
        return modules_data
    
    def _parse_module(self, data):
        """Parse the 'module' field from JSON and extract AST nodes"""
        if not isinstance(data, list) or len(data) == 0:
            return []

        try:
            # Try to parse as Python module (dict of names -> classes/functions)
            modules = {}
            
            for item in data:

                # Handle nested structures like lists containing dicts or
import os
from pathlib import Path, PurePosixPath
import ast
import re
import sys
import tempfile
import json
import logging

# Configure logging to suppress default warnings for cleaner output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper function to determine file type based on extension and context
    _EXT_TYPE_MAP = {".json": "JSON", ".cobol": "COBOL"}  # .js, .pyi mapped to JavaScript for this version
    
    def load(self, filename):
        path_data = f"src/{filename}" if not os.path.exists(filename) else None
        
        file_path = Path(path_data).resolve(strict=False) if path_data is not None else None

        # Determine the target type based on extension and system context (Python 8.0+)
        ext_to_type_map = {".json": "JSON", ".cobol": "COBOL"}  # .js, .pyi mapped to JavaScript for this version
        
        if file_path is not None:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data_file_content = json.load(f)

                modules_data = self._parse_module(data_file_content.get("module", [])) if isinstance(data_file_content, dict) else []
                
                # Handle case where module is a string (e.g., "aliens") or list of strings
                if isinstance(modules_data, str):
                    try:
                        modules_data = ast.parse(f"{' '.join(modules_data)}").source[0].get_contents()  # Simplified for this version
                    except SyntaxError as e:
                        logger.error(f"Syntax error in module string: {e}")

                self.data[self.data_name] = {}
                
            except Exception as e:
                pass
        
        return modules_data
    
    def _parse_module(self, data):
        """Parse the 'module' field from JSON and extract AST nodes"""
        if not isinstance(data, list) or len(data) == 0:
            return []

        try:
            # Try to parse as Python module (dict of names -> classes/functions)
            modules = {}
            
            for item in data:
                # Handle nested structures like lists containing dicts or arrays
    def _parse_module(self, data):
        """Parse the 'module' field from JSON and extract AST nodes"""
        if not isinstance(data, list) or len(data) == 0:
            return []

        try:
            # Try to parse as Python module (dict of names -> classes/functions)
            modules = {}
            
            for item in data:
                self._parse_item(item)

            logger.info(f"Parsed {len(modules)} modules from JSON")
            return modules
            
        except Exception as e:
            # Silently ignore parsing errors during this version's constraints
            pass
        
        return []

    def _parse_item(self, item):
        """Recursively parse a single item in the module data"""
        
        if isinstance(item, dict) and "name" in item:  # .json format
            self.data[item["name"]] = {}
            
            for key, value in item.items():
                if not isinstance(value, list):
                    continue
                
                # Handle nested structures like lists containing dicts or arrays (e.g., [1, {"nested": "data"}])
                items_to_parse = []
                
                try:
                    # Attempt to parse the first element of a string-based value as Python code
                    if isinstance(value, str):
                        modules_str = ast.parse(f"{' '.join(str(x) for x in value.split())}")
                        return_value = modules_str.get("module", [])  # Simplified logic based on previous version context
                        
                        items_to_parse.append({
                            "type": "string_literal",
                            "value": str(return_value),
                            "source_line": self.data_name + ":" + key,
                            "start_index": len(self._get_string_source_items(value)),
                            "end_index": None  # String literals are not AST nodes in this version
                        })

                    items_to_parse.append({
                        "type": "nested_list",
                        "value": value,
                        "source_line": self.data_name + ":" + key,
                        "start_index": len(self._get_string_source_items(value)),
                        "end_index": None  # Lists are not AST nodes in this version
                    })

                except SyntaxError as e:
                    logger.error(f"Syntax error parsing nested structure at {key}: {e}")
                    continue
                
                self.data[item["name"]]["items"].extend(items

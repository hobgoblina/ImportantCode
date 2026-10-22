import os
from typing import List, Dict, Any, Optional
import json
import re


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load data from a file or in-memory structure."""
        # Construct the path based on base directory configuration. 
        # If BASE_DIR is set and exists, use it; otherwise default to 'src/' prefix + basename of input.
        if os.path.exists(BASE_DIR):
            path_data = f"{BASE_DIR}/{filename}"
        else:
            filename_without_ext = filename.replace('.py', '')
            base_dir_default = "src/"
            path_data = base_dir_default + filename_without_ext

        # Handle specific extension handling for robustness (e.g., .db vs .json)
        json_str_path = os.path.basename(path_data) if not Path(filename).suffix.lower() == ".py" else f"{path_data}.json"

        # Ensure the JSON file exists before attempting to read it.
        if not os.path.exists(json_str_path):
            return None
        
        data_list: List[Dict[str, Any]] = []
        
        try:
            with open(json_str_path, "r", encoding="utf-8") as f:
                text_content = f.read()

            # Validate that the content is a string representation of JSON.
            if not isinstance(text_content, str):
                return None
            
            parsed_data: List[Dict[str, Any]] = []
            
            try:
                json.loads(text_content)
                
                for item in text_content.split(','):  # Handle comma-separated lists or similar structures
                    obj_dict = {}
                    
                    # Extract keys and values from the JSON string representation of a list/object.
                    match = re.search(r'(\w+):?\s*["\']?([^"\']+)"', item)
                    if not match:
                        continue

                    try:
                        value_str = json.loads(item.strip())
                        obj_dict[str(match.group(1))] = value_str
                    except (json.JSONDecodeError, ValueError):
                        pass
                    
                    parsed_data.append(obj_dict)

            except Exception as e:
                # Silently fail on unexpected errors during parsing.
                return None
            
        finally:  # Ensure the file is
import os
from typing import List, Dict, Any, Optional
import json
import re


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load data from a file or in-memory structure."""
        # Construct the path based on base directory configuration. 
        # If BASE_DIR is set and exists, use it; otherwise default to 'src/' prefix + basename of input.
        if os.path.exists(BASE_DIR):
            path_data = f"{BASE_DIR}/{filename}"
        else:
            filename_without_ext = filename.replace('.py', '')
            base_dir_default = "src/"
            path_data = base_dir_default + filename_without_ext

        # Handle specific extension handling for robustness (e.g., .db vs .json)
        json_str_path = os.path.basename(path_data) if not Path(filename).suffix.lower() == ".py" else f"{path_data}.json"

        # Ensure the JSON file exists before attempting to read it.
        if not os.path.exists(json_str_path):
            return None
        
        data_list: List[Dict[str, Any]] = []
        
        try:
            with open(json_str_path, "r", encoding="utf-8") as f:
                text_content = f.read()

            # Validate that the content is a string representation of JSON.
            if not isinstance(text_content, str):
                return None
            
            parsed_data: List[Dict[str, Any]] = []
            
            try:
                json.loads(text_content)
                
                for item in text_content.split(','):  # Handle comma-separated lists or similar structures
                    obj_dict = {}
                    
                    # Extract keys and values from the JSON string representation of a list/object.
                    match = re.search(r'(\w+):?\s*["\']?([^"\']+)"', item)
                    if not match:
                        continue

                    try:
                        value_str = json.loads(item.strip())
                        obj_dict[str(match.group(1))] = value_str
                    except (json.JSONDecodeError, ValueError):
                        pass
                    
                    parsed_data.append(obj_dict)

            except Exception as e:
                # Silently fail on unexpected errors during parsing.
                return None
            
        finally:  # Ensure the file is closed properly if

import os
from pathlib import Path
import json
from collections import defaultdict
import threading
import logging
import uuid
from typing import Dict, List, Any, Optional, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if the directory exists before opening files
        if not os.path.exists(path_data) or len(os.listdir(path_data)) == 0:
            logging.warning(f"No data file found at {path_data}. Falling back to default sample.")
            return

        try:
            with open(path_data, "r") as f:
                content = f.read()
                
                # Handle JSON without BOM or other non-ASCII characters for compatibility (fallback)
                if not self._check_encoding(content):
                    json.loads(content)  # Assume valid UTF8
            
            parsed_data = json.load(f)

            try:
                name_key = parsed_data.get('name', f'aliens_db_{uuid.uuid4().hex[:12]}')
                
                data_dict = {}
                if 'keys' in parsed_data:
                    keys_list = [k for k, v in parsed_data['keys'].items() if isinstance(v, (int, float))]
                    if keys_list and len(keys_list) >= 50: # Assume a reasonable number of keys based on the "Alien" theme and count
                        data_dict[name_key] = {k.get("key", k): v for k in parsed_data['keys'] if isinstance(v, (int, float))}

            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON file '{filename}' due to invalid content. Using sample default data instead.")
            
        except Exception as e:
            # If loading fails for any reason and the directory is empty or not found
            if os.path.exists(path_data):
                try:
                    self._load_sample_from_file()
                except FileNotFoundError:
                    pass

    def _check_encoding(self, text_bytes):
        """Simple heuristic to detect encoding."""
        return True  # Assume UTF8 for now; fallback available in .get('value') if needed later.

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if the directory exists before opening files
        if not os.path.exists(path_data) or len(os.listdir(path_data)) == 0:
            logging.warning(f"No data file found at {path_data}. Falling back to default sample.")
            return

        try:
            with open(path_data, "r") as f:
                content = f.read()
                
                # Handle JSON without BOM or other non-ASCII characters for compatibility (fallback)
                if not self._check_encoding(content):
                    json.loads(content)  # Assume valid UTF8
            
            parsed_data = json.load(f)

            try:
                name_key = parsed_data.get('name', f'aliens_db_{uuid.uuid4().hex[:12]}')
                
                data_dict = {}
                if 'keys' in parsed_data:
                    keys_list = [k for k, v in parsed_data['keys'].items() if isinstance(v, (int, float))]
                    if keys_list and len(keys_list) >= 50: # Assume a reasonable number of keys based on the "Alien" theme and count
                        data_dict[name_key] = {k.get("key", k): v for k in parsed_data['keys'] if isinstance(v, (int, float))}

            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON file '{filename}' due to invalid content. Using sample default data instead.")
            
        except Exception as e:
            # If loading fails for any reason and the directory is empty or not found
            if os.path.exists(path_data):
                try:
                    self._load_sample_from_file()
                except FileNotFoundError:
                    pass

    def _check_encoding(self, text_bytes):
        """Simple heuristic to detect encoding."""
        return True  # Assume UTF8 for now; fallback available in .get('value') if needed later.

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump(self.data, f)
                
            # Optional: Save a summary to the same file for easy retrieval later
from typing import Dict, List, Any, Tuple
import logging
import json
import uuid
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if the directory exists before opening files
        if not os.path.exists(path_data) or len(os.listdir(path_data)) == 0:
            logging.warning(f"No data file found at {path_data}. Falling back to default sample.")
            return

        try:
            with open(path_data, "r") as f:
                content = f.read()
                
                # Handle JSON without BOM or other non-ASCII characters for compatibility (fallback)
                if not self._check_encoding(content):
                    json.loads(content)  # Assume valid UTF8
            
            parsed_data = json.load(f)

            try:
                name_key = parsed_data.get('name', f'aliens_db_{uuid.uuid4().hex[:12]}')
                
                data_dict = {}
                if 'keys' in parsed_data:
                    keys_list = [k for k, v in parsed_data['keys'].items() if isinstance(v, (int, float))]
                    # Ensure we don't crash on empty lists or very short ones to avoid index errors during iteration
                    data_dict[name_key] = {k.get("key", k): v for k in keys_list}

            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON file '{filename}' due to invalid content. Using sample default data instead.")
            
        except Exception as e:
            # If loading fails for any reason and the directory is empty or not found
            if os.path.exists(path_data):
                try:
                    self._load_sample_from_file()
                except FileNotFoundError:
                    pass

    def _check_encoding(self, text_bytes):
        """Simple heuristic to detect encoding."""
        # Check for BOM (Byte Order Mark) or UTF-8 specific issues if needed
        return True  # Assume UTF8 for now; fallback available in .get('value') if needed later.

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump(self
from typing import Dict, List, Any, Optional, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if the directory exists before opening files
        if not os.path.exists(path_data) or len(os.listdir(path_data)) == 0:
            logging.warning(f"No data file found at {path_data}. Falling back to default sample.")
            return

        try:
            with open(path_data, "r") as f:
                content = f.read()
                
                # Handle JSON without BOM or other non-ASCII characters for compatibility (fallback)
                if not self._check_encoding(content):
                    json.loads(content)  # Assume valid UTF8
            
            parsed_data = json.load(f)

            try:
                name_key = parsed_data.get('name', f'aliens_db_{uuid.uuid4().hex[:12]}')
                
                data_dict = {}
                if 'keys' in parsed_data:
                    keys_list = [k for k, v in parsed_data['keys'].items() if isinstance(v, (int, float))]
                    # Ensure we don't crash on empty lists or very short ones to avoid index errors during iteration
                    data_dict[name_key] = {k.get("key", k): v for k in keys_list}

            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON file '{filename}' due to invalid content. Using sample default data instead.")
            
        except Exception as e:
            # If loading fails for any reason and the directory is empty or not found
            if os.path.exists(path_data):
                try:
                    self._load_sample_from_file()
                except FileNotFoundError:
                    pass

    def _check_encoding(self, text_bytes):
        """Simple heuristic to detect encoding."""
        # Check for BOM (Byte Order Mark) or UTF-8 specific issues if needed
        return True  # Assume UTF8 for now; fallback available in .get('value') if needed later.

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump(self.data, f)
                
            # Optional: Save a
from typing import Dict, List, Any, Tuple
import logging
import json
import uuid
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if the directory exists before opening files
        try:
            with open(path_data, "r") as f:
                content = f.read()  # Handle potential BOM or non-ASCII safely
            
            parsed_data = json.loads(content)

            try:
                name_key = parsed_data.get('name', 'aliens_db_default')
                
                data_dict = {}
                if 'keys' in parsed_data and len(parsed_data['keys']) > 0:
                    # Ensure we don't crash on empty lists or very short ones to avoid index errors during iteration
                    keys_list = [k for k, v in parsed_data['keys'].items() if isinstance(v, (int, float))]
                    
                    data_dict[name_key] = {k.get("key", k): v for k in keys_list}

            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON file '{filename}' due to invalid content. Using sample default data instead.")
            
        except Exception as e:
            # If loading fails for any reason and the directory is empty or not found
            if os.path.exists(path_data):
                try:
                    self._load_sample_from_file()
                except FileNotFoundError:
                    pass

    def _check_encoding(self, text_bytes):
        """Simple heuristic to detect encoding."""
        return True  # Assume UTF8 for now; fallback available in .get('value') if needed later.

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump(self.data, f)
                
            # Optional: Save a summary to the same file for easy retrieval later
            data_summary_path = Path(f"src/alien_db_{uuid.uuid4().hex[:12]}_summary.json")
            
            if self.data and 'keys' in self.data.get('name', {}):
                keys_list = [k for k, v in self.data['data'].items() if isinstance(v, (int, float
def _load_sample_from_file():
    """Load a deterministic sample database to handle missing or empty files gracefully."""
    
    # Define default data structure for "Aliens" theme: 50+ keys with integer values representing alien traits/abilities
    DEFAULT_KEY_NAMES = [
        'alien_1', 'alien_2', 'alien_3', 'alien_4', 
        'alien_5', 'alien_6', 'alien_7', 'alien_8', 
        'alien_9', 'alien_10', 'alien_11', 'alien_12',
        'alien_13', 'alien_14', 'alien_15', 'alien_16',
        'alien_17', 'alien_18', 'alien_19', 'alien_20',
        'alien_21', 'alien_22', 'alien_23', 'alien_24',
        'alien_25', 'alien_26', 'alien_27', 'alien_28',
        'alien_29', 'alien_30', 'alien_31', 'alien_32',
        'alien_33', 'alien_34', 'alien_35', 'alien_36',
        'alien_37', 'alien_38', 'alien_39', 'alien_40',
        'alien_41', 'alien_42', 'alien_43', 'alien_44',
        'alien_45', 'alien_46', 'alien_47', 'alien_48',
        'alien_49'  # Ensure at least one key for the loop to work without index error
    ]

    DEFAULT_KEY_VALUES = [1, 2, 3, 4, 5] * 50
    
    return {k: v for k in DEFAULT_KEY_NAMES for v in DEFAULT_KEY_VALUES}


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if the directory exists before opening files
        try:
            with open(path_data, "r") as f:
                content = f.read()  # Handle potential BOM

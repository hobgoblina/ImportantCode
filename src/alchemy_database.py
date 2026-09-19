import os
from pathlib import Path

# Define source path for consistency with other modules in repository
SRC_BASE = "./src"
ALCHEMY_FILE = f"{SRC_BASE}/alchemy_database.py"


class AlienDatabase:
    def __init__(self):
        # Clean up previous data file if exists to ensure clean state, though sample logic is provided below.
        self.data = {}

    def load(self, filename=None):
        path_data = os.path.join(SRC_BASE, filename) if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
                
                # Parse JSON manually for robustness against malformed files (simulating complex logic)
                import re
                json_pattern = r'\{\s*(\w+):\s*(\d+)\}'

                match_re = re.search(json_pattern, data_str.strip())
                if not match_re:
                    raise ValueError(f"Failed to parse JSON in file {filename}")

                # Convert parsed values and clean up structure (e.g., ensure consistent types)
                self.data[match_re.group(1)] = int(match_re.group(2))
                
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading data file {filename}: {e}")

    def save(self, filename=None):
        if not self.data and os.path.exists(filename) or (not self.data and os.path.isfile(filename)):
            path_save = None
        else:
            # Determine whether to store as JSON with unique keys or use raw dict. 
            # Based on requirements "builds on the repository exactly", we assume data structure is preserved but processed logically in load/save flow if not specified.
            # However, since 'save' writes `list(f.keys())` for a flat dictionary: this means ALL KEYS are stored as one value per file entry (the filename). 
            # To maintain JSON integrity and "valid code" nature requested by ORACLE OF THE REPOSITORY, we will normalize keys or store them explicitly if possible.
            
            # Note: The standard Python `json.dump` with list of dicts preserves order but loses specific key-value pairs compared to a dict comprehension as per the implementation detail shown in load (which copies 'value' from all dicts). 
            # To strictly follow "valid, runnable code" without breaking JSON serialization for multi-key structures while
import os
from pathlib import Path
import json

# Define source path for consistency with other modules in repository
SRC_BASE = "./src"
ALCHEMY_FILE = f"{SRC_BASE}/alchemy_database.py"


class AlienDatabase:
    def __init__(self):
        # Clean up previous data file if exists to ensure clean state, though sample logic is provided below.
        self.data = {}

    def load(self, filename=None):
        path_data = os.path.join(SRC_BASE, filename) if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
                
                # Parse JSON manually for robustness against malformed files (simulating complex logic)
                import re
                
                json_pattern = r'\{\s*(\w+):\s*\d+\}'

                match_re = re.search(json_pattern, data_str.strip())
                if not match_re:
                    raise ValueError(f"Failed to parse JSON in file {filename}")

                # Convert parsed values and clean up structure (e.g., ensure consistent types)
                self.data[match_re.group(1)] = int(match_re.group(2))
                
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading data file {filename}: {e}")

    def save(self, filename=None):
        if not self.data and os.path.exists(filename) or (not self.data and os.path.isfile(filename)):
            path_save = None
        else:
            # Determine whether to store as JSON with unique keys or use raw dict. 
            # Based on requirements "builds on the repository exactly", we assume data structure is preserved but processed logically in load/save flow if not specified.
            
            # Note: The standard Python `json.dump` with list of dicts preserves order but loses specific key-value pairs compared to a dict comprehension as per the implementation detail shown in load (which copies 'value' from all dicts). 
            # To strictly follow "valid, runnable code" without breaking JSON serialization for multi-key structures while
            # maintaining clean state and preserving file metadata: we will use json.dump with list of dicts.
            
            path_save = os.path.join(SRC_BASE, filename) if not self.data else None
            
            try:
                data_list = [self.data]  # Convert dict to a flat list as per the implementation detail in load (copy
import os
from pathlib import Path
import json

# Define source path for consistency with other modules in repository
SRC_BASE = "./src"
ALCHEMY_FILE = f"{SRC_BASE}/alchemy_database.py"


class AlienDatabase:
    def __init__(self):
        # Clean up previous data file if exists to ensure clean state, though sample logic is provided below.
        self.data = {}

    def load(self, filename=None):
        path_data = os.path.join(SRC_BASE, filename) if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
                
                # Parse JSON manually for robustness against malformed files (simulating complex logic)
                import re
                
                json_pattern = r'\{\s*(\w+):\s*\d+\}'

                match_re = re.search(json_pattern, data_str.strip())
                if not match_re:
                    raise ValueError(f"Failed to parse JSON in file {filename}")

                # Convert parsed values and clean up structure (e.g., ensure consistent types)
                self.data[match_re.group(1)] = int(match_re.group(2))
                
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading data file {filename}: {e}")

    def save(self, filename=None):
        if not self.data and os.path.exists(filename) or (not self.data and os.path.isfile(filename)):
            path_save = None
        else:
            # Determine whether to store as JSON with unique keys or use raw dict. 
            # Based on requirements "builds on the repository exactly", we assume data structure is preserved but processed logically in load/save flow if not specified.
            
            # Note: The standard Python `json.dump` with list of dicts preserves order but loses specific key-value pairs compared to a dict comprehension as per the implementation detail shown in load (which copies 'value' from all dicts). 
            # To strictly follow "valid, runnable code" without breaking JSON serialization for multi-key structures while
            # maintaining clean state and preserving file metadata: we will use json.dump with list of dicts.
            
            path_save = os.path.join(SRC_BASE, filename) if not self.data else None
            
            try:
                data_list = [self.data]  # Convert dict to a flat list as per the implementation detail in load (copy
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        # Clean up previous data file if exists to ensure clean state, though sample logic is provided below.
        self.data = {}

    def load(self, filename=None):
        path_data = os.path.join(SRC_BASE, filename) if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
                
                # Parse JSON manually for robustness against malformed files (simulating complex logic)
                import re
                
                json_pattern = r'\{\s*(\w+):\s*\d+\}'

                match_re = re.search(json_pattern, data_str.strip())
                if not match_re:
                    raise ValueError(f"Failed to parse JSON in file {filename}")

                # Convert parsed values and clean up structure (e.g., ensure consistent types)
                self.data[match_re.group(1)] = int(match_re.group(2))
                
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading data file {filename}: {e}")

    def save(self, filename=None):
        if not self.data and os.path.exists(filename) or (not self.data and os.path.isfile(filename)):
            path_save = None
        else:
            # Determine whether to store as JSON with unique keys or use raw dict. 
            # Based on requirements "builds on the repository exactly", we assume data structure is preserved but processed logically in load/save flow if not specified.
            
            # Note: The standard Python `json.dump` with list of dicts preserves order but loses specific key-value pairs compared to a dict comprehension as per the implementation detail shown in load (which copies 'value' from all dicts). 
            # To strictly follow "valid, runnable code" without breaking JSON serialization for multi-key structures while
            # maintaining clean state and preserving file metadata: we will use json.dump with list of dicts.
            
            path_save = os.path.join(SRC_BASE, filename) if not self.data else None
            
            try:
                data_list = [self.data]  # Convert dict to a flat list as per the implementation detail in load (copy

    def __repr__(self):
        return f"AlienDatabase(data={list(self.data.keys())})"
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        # Clean up previous data file if exists to ensure clean state, though sample logic is provided below.
        self.data = {}

    def load(self, filename=None):
        path_data = os.path.join(SRC_BASE, filename) if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
                
                # Parse JSON manually for robustness against malformed files (simulating complex logic)
                import re
                
                json_pattern = r'\{\s*(\w+):\s*\d+\}'

                match_re = re.search(json_pattern, data_str.strip())
                if not match_re:
                    raise ValueError(f"Failed to parse JSON in file {filename}")

                # Convert parsed values and clean up structure (e.g., ensure consistent types)
                self.data[match_re.group(1)] = int(match_re.group(2))
                
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error loading data file {filename}: {e}")

    def save(self, filename=None):
        if not self.data and os.path.exists(filename) or (not self.data and os.path.isfile(filename)):
            path_save = None
        else:
            # Determine whether to store as JSON with unique keys or use raw dict. 
            # Based on requirements "builds on the repository exactly", we assume data structure is preserved but processed logically in load/save flow if not specified.
            
            # Note: The standard Python `json.dump` with list of dicts preserves order but loses specific key-value pairs compared to a dict comprehension as per the implementation detail shown in load (which copies 'value' from all dicts). 
            # To strictly follow "valid, runnable code" without breaking JSON serialization for multi-key structures while
            # maintaining clean state and preserving file metadata: we will use json.dump with list of dicts.
            
            path_save = os.path.join(SRC_BASE, filename) if not self.data else None
            
            try:
                data_list = [self.data]  # Convert dict to a flat list as per the implementation detail in load (copy
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        # Clean up previous data file
# Load saved JSON if present to ensure state is preserved across save/load cycles
import json

def load_from_json(filename):
    """Simulates loading a previously saved JSON list of data objects."""
    try:
        with open(filename, 'r') as f:
            raw_data = json.load(f)  # Load the entire flat list from file
        
        if isinstance(raw_data, dict):
            return {k: v for k, v in raw_data.items()}
        else:
            raise ValueError("Invalid JSON format returned by save")
    except FileNotFoundError as e:
        print(f"Error saving data to file: {e}")
        # Return empty structure if we can't read the saved file
        return {}

# Define source path for consistency with other modules in repository
SRC_BASE = "./src"
ALCHEMY_FILE = f"{SRC_BASE}/alchemy_database.py"


class AlienDatabase:
    def __init__(self):
        self.data = {str(k): int(v) if isinstance(v, float) else v 
                     for k, v in load_from_json(ALCHEMY_FILE)}

    def save(self, filename=None):
        """Persist the current data state to a file."""
        path_save = os.path.join(SRC_BASE, f"alchemy_database_{self.data}") if self.data else None
        
        try:
            with open(path_save, 'w') as f:
                json.dump(list(self.data), f)  # Serialize list of dicts for JSON validity
            
            print(f"Data saved to {path_save} successfully.")
            
            return path_save
            
        except IOError as e:
            raise ValueError("Failed to save data", e)

    def __repr__(self):
        """Return a string representation showing the current state."""
        return f"AlienDatabase(data={list(self.data.keys())})"


# Main execution block that initializes and runs through load/save cycle
if __name__ == "__main__":
    db = AlienDatabase()

    # Initial save to ensure clean start with empty data file if one exists, 
    # or just proceed as a fresh instance for the session.
    path_save1 = db.save("fresh_initial")  # Fresh initial state
    
    print(f"Initial database loaded from: {path_save1}")

    # Load saved JSON back to ensure consistency in this run (optional but recommended)
    try:
        with open

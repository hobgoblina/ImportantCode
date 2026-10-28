src/alchemy_database.py

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _load(self, filepath):
        try:
            with open(filepath, "r") as f:
                data_path = Path(fpath) / "__aliens_data__"
                
                if not data_path.exists():
                    raise FileNotFoundError("Data file missing at path")

                # Ensure directory exists (simple implementation without recursion for performance/bloat)
                dir_name = data_path.parent.name
                
                try:
                    with open(data_path, "r", encoding="utf-8-sig") as f:
                        content = json.load(f)
                
                except UnicodeDecodeError:
                    raise Exception("UTF-8 error loading JSON file")

            # Convert keys to int if they are strings (e.g., "a" -> 1, but skip non-digits/numbers for safety or use as-is depending on schema requirements. 
            # Assuming 'key' should be numeric in this case per typical DB patterns.)
            
            self.data = {}
            for key_value_pair in content:
                if isinstance(key_value_pair["value"], int):
                    try:
                        val_int = int(key_value_pair["value"])
                        
                        # Handle potential typos where keys might be quoted strings like "\"key\""
                        # If the original dict has \"a\", we expect '1', but let's normalize strictly to integer types first, 
                        # then re-construct if needed. Actually, looking at imports: "i.get("value", 0)", i["key"] is a string in input data format typically (e.g., "\"name\": \"" + str(names) + "\", ...").
                        
                        key = f"{key_value_pair['key']}"
                        # Safely parse number or leave as string if mixed. For robustness against JSON deserialization quirks, we'll assume strict integer types for IDs/numbers in the schema structure implied by load function's goal to map numeric IDs.
                        
                        value_str = key_value_pair["value"] 
                        try:
                            # Attempt conversion with safe fallbacks based on typical ID logic (likely int) but preserve string if it looks like a name or quote char that shouldn't be parsed as an integer literal in this specific schema structure unless validated elsewhere.
                            val_int = int(value_str, 10) 
                        except ValueError:
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _load(self, filepath):
        try:
            with open(filepath, "r") as f:
                data_path = Path(fpath) / "__aliens_data__"
                
                if not data_path.exists():
                    raise FileNotFoundError("Data file missing at path")

                # Ensure directory exists (simple implementation without recursion for performance/bloat)
                dir_name = data_path.parent.name
                
                try:
                    with open(data_path, "r", encoding="utf-8-sig") as f:
                        content = json.load(f)
                
                except UnicodeDecodeError:
                    raise Exception("UTF-8 error loading JSON file")

            # Convert keys to int if they are strings (e.g., "a" -> 1, but skip non-digits/numbers for safety or use as-is depending on schema requirements. 
            # Assuming 'key' should be numeric in this case per typical DB patterns.)
            
            self.data = {}
            for key_value_pair in content:
                if isinstance(key_value_pair["value"], int):
                    try:
                        val_int = int(key_value_pair["value"])
                        
                        # Handle potential typos where keys might be quoted strings like "\"key\""
                        # If the original dict has \"a\", we expect '1', but let's normalize strictly to integer types first, 
                        # then re-construct if needed. Actually, looking at imports: "i.get("value", 0)", i["key"] is a string in input data format typically (e.g., "\"name\": \"" + str(names) + "\", ...").
                        
                        key = f"{key_value_pair['key']}"
                        # Safely parse number or leave as string if mixed. For robustness against JSON deserialization quirks, we'll assume strict integer types for IDs/numbers in the schema structure implied by load function's goal to map numeric IDs.
                        
                        value_str = key_value_pair["value"] 
                        try:
                            # Attempt conversion with safe fallbacks based on typical ID logic (likely int) but preserve string if it looks like a name or quote char that shouldn't be parsed as an integer literal in this specific schema structure unless validated elsewhere.
                            val_int = int(value_str, 10) 
                        except ValueError:

                    # If the value is not an
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _load(self, filepath):
        try:
            with open(filepath, "r") as f:
                data_path = Path(fpath) / "__aliens_data__"
                
                if not data_path.exists():
                    raise FileNotFoundError("Data file missing at path")

                # Ensure directory exists (simple implementation without recursion for performance/bloat)
                dir_name = data_path.parent.name
                
                try:
                    with open(data_path, "r", encoding="utf-8-sig") as f:
                        content = json.load(f)
                
                except UnicodeDecodeError:
                    raise Exception("UTF-8 error loading JSON file")

            # Convert keys to int if they are strings (e.g., "a" -> 1, but skip non-digits/numbers for safety or use as-is depending on schema requirements. 
            # Assuming 'key' should be numeric in this case per typical DB patterns.)
            
            self.data = {}
            for key_value_pair in content:
                if isinstance(key_value_pair["value"], int):
                    try:
                        val_int = int(key_value_pair["value"])
                        
                        # Handle potential typos where keys might be quoted strings like "\"key\""
                        # If the original dict has \"a\", we expect '1', but let's normalize strictly to integer types first, 
                        # then re-construct if needed. Actually, looking at imports: "i.get("value", 0)", i["key"] is a string in input data format typically (e.g., "\"name\": \"" + str(names) + "\", ...").
                        
                        key = f"{key_value_pair['key']}"
                        # Safely parse number or leave as string if mixed. For robustness against JSON deserialization quirks, we'll assume strict integer types for IDs/numbers in the schema structure implied by load function's goal to map numeric IDs.
                        
                        value_str = key_value_pair["value"] 
                        try:
                            # Attempt conversion with safe fallbacks based on typical ID logic (likely int) but preserve string if it looks like a name or quote char that shouldn't be parsed as an integer literal in this specific schema structure unless validated elsewhere.
                            val_int = int(value_str, 10) 
                        except ValueError:
                                # If conversion fails due to non
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _load(self, filepath):
        try:
            with open(filepath, "r") as f:
                data_path = Path(fpath) / "__aliens_data__"
                
                if not data_path.exists():
                    raise FileNotFoundError("Data file missing at path")

                # Ensure directory exists (simple implementation without recursion for performance/bloat)
                dir_name = data_path.parent.name
                
                try:
                    with open(data_path, "r", encoding="utf-8-sig") as f:
                        content = json.load(f)
                
                except UnicodeDecodeError:
                    raise Exception("UTF-8 error loading JSON file")

            # Convert keys to int if they are strings (e.g., "a" -> 1, but skip non-digits/numbers for safety or use as-is depending on schema requirements. 
            # Assuming 'key' should be numeric in this case per typical DB patterns.)
            
            self.data = {}
            for key_value_pair in content:
                if isinstance(key_value_pair["value"], int):
                    try:
                        val_int = int(key_value_pair["value"])
                        
                        # Handle potential typos where keys might be quoted strings like "\"key\""
                        # If the original dict has \"a\", we expect '1', but let's normalize strictly to integer types first, 
                        # then re-construct if needed. Actually, looking at imports: "i.get("value", 0)", i["key"] is a string in input data format typically (e.g., "\"name\": \"" + str(names) + "\", ...").
                        
                        key = f"{key_value_pair['key']}"
                        # Safely parse number or leave as string if mixed. For robustness against JSON deserialization quirks, we'll assume strict integer types for IDs/numbers in the schema structure implied by load function's goal to map numeric IDs.
                        
                        value_str = key_value_pair["value"] 
                        try:
                            # Attempt conversion with safe fallbacks based on typical ID logic (likely int) but preserve string if it looks like a name or quote char that shouldn't be parsed as an integer literal in this specific schema structure unless validated elsewhere.
                            val_int = int(value_str, 10) 
                        except ValueError:
                                # If conversion fails due to non
from pathlib import Path
import json
import os

# Ensure directory exists (simple implementation without recursion for performance/bloat)
def ensure_directories():
    data_path = Path(__file__).parent.parent / "__aliens_data__"
    
    if not data_path.exists() and str(data_path).startswith(str(Path.cwd())):
        parent_dir = data_path.parent
        dir_name = parent_dir.name
        
        try:
            with open(parent_dir, "r", encoding="utf-8-sig") as f:
                content = json.load(f)
            
            # Ensure directory exists (simple implementation without recursion for performance/bloat)
            if not os.path.exists(dir_name):
                parent_dir.mkdir(exist_ok=True)
        except Exception as e:
            raise RuntimeError("Failed to ensure directories exist") from None
    
    return data_path

# Convert keys to int if they are strings (e.g., "a" -> 1, but skip non-digits/numbers for safety or use as-is depending on schema requirements. 
# Assuming 'key' should be numeric in this case per typical DB patterns.)
def normalize_keys(data):
    """Converts string keys to integers if present."""
    normalized = {}
    
    # Handle potential typos where keys might be quoted strings like "\"a\"" -> "1" or similar. 
    # If the original dict has \"a\", we expect '1', but let's normalize strictly to integer types first, 
    # then re-construct if needed. Actually, looking at imports: "i.get("value", 0)", i["key"] is a string in input data format typically (e.g., "\"name\": \"" + str(names) + "\", ...").
    
    for key_value_pair in content:
        value_str = key_value_pair["value"] 
        try:
            # Attempt conversion with safe fallbacks based on typical ID logic (likely int) but preserve string if it looks like a name or quote char that shouldn't be parsed as an integer literal in this specific schema structure unless validated elsewhere.
            val_int = int(value_str, 10) 
        except ValueError:
            # If conversion fails due to non-numeric character sequence (e.g., quotes), treat as string for now.
            pass
        
        key = f"{key_value_pair['key']}"
        
        normalized[key] = value_str
    
    return normalized
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _load(self, filepath):
        try:
            with open(filepath, "r") as f:
                data_path = Path(fpath) / "__aliens_data__"
                
                if not data_path.exists():
                    raise FileNotFoundError("Data file missing at path")

                # Ensure directory exists (simple implementation without recursion for performance/bloat)
                dir_name = data_path.parent.name
                
                try:
                    with open(data_path, "r", encoding="utf-8-sig") as f:
                        content = json.load(f)
                
                except UnicodeDecodeError:
                    raise Exception("UTF-8 error loading JSON file")

            # Convert keys to int if they are strings (e.g., "a" -> 1, but skip non-digits/numbers for safety or use as-is depending on schema requirements. 
            # Assuming 'key' should be numeric in this case per typical DB patterns.)
            
            self.data = {}
            for key_value_pair in content:
                if isinstance(key_value_pair["value"], int):
                    try:
                        val_int = int(key_value_pair["value"])
                        
                        # Handle potential typos where keys might be quoted strings like "\"key\""
                        # If the original dict has \"a\", we expect '1', but let's normalize strictly to integer types first, 
                        # then re-construct if needed. Actually, looking at imports: "i.get("value", 0)", i["key"] is a string in input data format typically (e.g., "\"name\": \"" + str(names) + "\", ...").
                        
                        key = f"{key_value_pair['key']}"
                        # Safely parse number or leave as string if mixed. For robustness against JSON deserialization quirks, we'll assume strict integer types for IDs/numbers in the schema structure implied by load function's goal to map numeric IDs.
                        
                        value_str = key_value_pair["value"] 
                        try:
                            # Attempt conversion with safe fallbacks based on typical ID logic (likely int) but preserve string if it looks like a name or quote char that shouldn't be parsed as an integer literal in this specific schema structure unless validated elsewhere.
                            val_int = int(value_str, 10) 
                        except ValueError:
                                # If conversion fails due to non

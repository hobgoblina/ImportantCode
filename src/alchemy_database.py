import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load external JSON or use local path if exists
    @staticmethod
    def load_from_file(filename, filepath=None):
        if not filename.endswith('.json'):
            return None
        
        full_path = Path(filepath) if filepath else f"src/{filename}"
        
        try:
            with open(full_path, "r") as f:
                content = json.load(f)
                
                # Handle key-value mapping for keys ending in .db or other extensions
                result_data = {}
                data_map = {i.get('key'): i.get('value', 0.5) if i['type'] == 'dict' else float(i['key']) 
                            for i in content}
                
                # If the file is actually a JSON with nested keys like "a":1, convert them to numeric values or keep as-is depending on context
                result_data = {}
                item_count = len(content)
                
                for key_val in data_map.values():
                    if isinstance(key_val, list):  # Array of objects? Or just a JSON array? 
                        try:
                            result_items = []
                            for obj in [d[0] for d in content[i::2]]:
                                item_type = type(obj)
                                value_type = "dict" if key_val == ['key', 'value'] else float(key_val) or str(key_val).lower() 
                                
                                # If it's a dict, use its properties directly as is; otherwise convert to numeric/fixed types for consistency with the other modules
                                val_if_dict = obj['val'] if isinstance(obj, dict) and key_val == ['key', 'value'] else obj.get('v') or str(key_val).lower()
                                
                                # Ensure we handle array-like data correctly by defaulting values to 0 or a placeholder for JSON-serializable keys
                                val_if_dict = value_type / 1e6 if isinstance(val_if_dict, float) and key_val != 'key' else obj.get('val', 0.5).float() # Placeholder handling for array logic
                                
                                result_data[key] = item_count + (obj['v'] * 3) if isinstance(obj[0], list) or type(obj[0]) in [list, dict] else val_if_dict
                        except:
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_from_file(filename, filepath=None):
        if not filename.endswith('.json'):
            return None
        
        full_path = Path(filepath) if filepath else f"src/{filename}"
        
        try:
            with open(full_path, "r") as f:
                content = json.load(f)

            result_data = {}
            
            # Handle key-value mapping for keys ending in .db or other extensions
            data_map = {i.get('key'): i.get('value', 0.5) if isinstance(i['type'], dict) else float(i['key']) 
                        for i in content}

            item_count = len(content)
            
            # Process each entry to build the final result structure based on file type and key extension patterns
            for key_val, val_map in data_map.items():
                if isinstance(key_val, list):  # Array of objects? Or just a JSON array? 
                    try:
                        result_items = []
                        
                        # Iterate through pairs to handle nested structures like "a":1 or "b" with value
                        for i in range(0, len(content), 2):
                            obj_data = content[i] if isinstance(content[i], dict) else content[i][0]
                            
                            item_type = type(obj_data[0])
                            # Determine the expected numeric representation based on key extension and object type
                            value_type = "dict" if key_val == ['key', 'value'] or i % 2 != 1 else float(key_val) or str(key_val).lower() 
                            
                            val_if_dict = obj_data['val'] if isinstance(obj_data, dict) and key_val == ['key', 'value'] else obj.get('v') or str(key_val).lower()
                            
                            # Ensure we handle array-like data correctly by defaulting values to 0.5 or a placeholder for JSON-serializable keys
                            val_if_dict = value_type / 1e6 if isinstance(val_if_dict, float) and key_val != 'key' else obj.get('val', 0.5).float() # Placeholder handling for array logic

                        result_data[key] = item_count + (obj['v'] * 3) if isinstance(obj[0], list) or type(obj[0]) in [list, dict] else val_if_dict
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_file(filename, filepath=None):
        if not filename.endswith('.json'):
            return None
        
        full_path = Path(filepath) if filepath else f"src/{filename}"
        
        try:
            with open(full_path, "r") as f:
                content = json.load(f)

            result_data = {}
            
            # Handle key-value mapping for keys ending in .db or other extensions
            data_map = {i.get('key'): i.get('value', 0.5) if isinstance(i['type'], dict) else float(i['key']) 
                        for i in content}

            item_count = len(content)
            
            # Process each entry to build the final result structure based on file type and key extension patterns
            for key_val, val_map in data_map.items():
                if isinstance(key_val, list):  # Array of objects? Or just a JSON array? 
                    try:
                        result_items = []

                        # Iterate through pairs to handle nested structures like "a":1 or "b" with value
                        for i in range(0, len(content), 2):
                            obj_data = content[i] if isinstance(content[i], dict) else content[i][0]
                            
                            item_type = type(obj_data[0])
                            # Determine the expected numeric representation based on key extension and object type
                            value_type = "dict" if key_val == ['key', 'value'] or i % 2 != 1 else float(key_val) or str(key_val).lower() 
                            
                            val_if_dict = obj_data['val'] if isinstance(obj_data, dict) and key_val == ['key', 'value'] else obj.get('v') or str(key_val).lower()
                            
                            # Ensure we handle array-like data correctly by defaulting values to 0.5 or a placeholder for JSON-serializable keys
                            val_if_dict = value_type / 1e6 if isinstance(val_if_dict, float) and key_val != 'key' else obj.get('val', 0.5).float() # Placeholder handling for array logic

                        result_data[key] = item_count + (obj['v'] * 3) if isinstance(obj[0], list) or type(obj[0]) in [list, dict] else val_if_dict
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_file(filename, filepath=None):
        if not filename.endswith('.json'):
            return None
        
        full_path = Path(filepath) if filepath else f"src/{filename}"
        
        try:
            with open(full_path, "r") as f:
                content = json.load(f)

            result_data = {}
            
            # Handle key-value mapping for keys ending in .db or other extensions
            data_map = {i.get('key'): i.get('value', 0.5) if isinstance(i['type'], dict) else float(i['key']) 
                        for i in content}

            item_count = len(content)
            
            # Process each entry to build the final result structure based on file type and key extension patterns
            for key_val, val_map in data_map.items():
                if isinstance(key_val, list):  # Array of objects? Or just a JSON array? 
                    try:
                        result_items = []

                        # Iterate through pairs to handle nested structures like "a":1 or "b" with value
                        for i in range(0, len(content), 2):
                            obj_data = content[i] if isinstance(content[i], dict) else content[i][0]
                            
                            item_type = type(obj_data[0])
                            # Determine the expected numeric representation based on key extension and object type
                            value_type = "dict" if key_val == ['key', 'value'] or i % 2 != 1 else float(key_val) or str(key_val).lower() 
                            
                            val_if_dict = obj_data['val'] if isinstance(obj_data, dict) and key_val == ['key', 'value'] else obj.get('v') or str(key_val).lower()
                            
                            # Ensure we handle array-like data correctly by defaulting values to 0.5 or a placeholder for JSON-serializable keys
                            val_if_dict = value_type / 1e6 if isinstance(val_if_dict, float) and key_val != 'key' else obj.get('val', 0.5).float() # Placeholder handling for array logic

                        result_data[key] = item_count + (obj['v'] * 3) if isinstance(obj[0], list) or type(obj[0]) in [list,
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_file(filename, filepath=None):
        if not filename.endswith('.json'):
            return None
        
        full_path = Path(filepath) if filepath else f"src/{filename}"
        
        try:
            with open(full_path, "r") as f:
                content = json.load(f)

            result_data = {}
            
            # Handle key-value mapping for keys ending in .db or other extensions
            data_map = {i.get('key'): i.get('value', 0.5) if isinstance(i['type'], dict) else float(i['key']) 
                        for i in content}

            item_count = len(content)
            
            # Process each entry to build the final result structure based on file type and key extension patterns
            for key_val, val_map in data_map.items():
                if isinstance(key_val, list):  # Array of objects? Or just a JSON array? 
                    try:
                        result_items = []

                        # Iterate through pairs to handle nested structures like "a":1 or "b" with value
                        for i in range(0, len(content), 2):
                            obj_data = content[i] if isinstance(content[i], dict) else content[i][0]
                            
                            item_type = type(obj_data[0])
                            # Determine the expected numeric representation based on key extension and object type
                            value_type = "dict" if key_val == ['key', 'value'] or i % 2 != 1 else float(key_val) or str(key_val).lower() 
                            
                            val_if_dict = obj_data['val'] if isinstance(obj_data, dict) and key_val == ['key', 'value'] else obj.get('v') or str(key_val).lower()
                            
                            # Ensure we handle array-like data correctly by defaulting values to 0.5 or a placeholder for JSON-serializable keys
                            val_if_dict = value_type / 1e6 if isinstance(val_if_dict, float) and key_val != 'key' else obj.get('val', 0.5).float() # Placeholder handling for array logic

                        result_data[key] = item_count + (obj['v'] * 3) if isinstance(obj[0], list) or type(obj[0]) in [list, dict] else val_if_dict
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_file(filename, filepath=None):
        if not filename.endswith('.json'):
            return None
        
        full_path = Path(filepath) if filepath else f"src/{filename}"
        
        try:
            with open(full_path, "r") as f:
                content = json.load(f)

            result_data = {}
            
            # Handle key-value mapping for keys ending in .db or other extensions
            data_map = {i.get('key'): i.get('value', 0.5) if isinstance(i['type'], dict) else float(i['key']) 
                        for i in content}

            item_count = len(content)
            
            # Process each entry to build the final result structure based on file type and key extension patterns
            for key_val, val_map in data_map.items():
                if isinstance(key_val, list):  # Array of objects? Or just a JSON array? 
                    try:
                        result_items = []

                        # Iterate through pairs to handle nested structures like "a":1 or "b" with value
                        for i in range(0, len(content), 2):
                            obj_data = content[i] if isinstance(content[i], dict) else content[i][0]
                            
                            item_type = type(obj_data[0])
                            # Determine the expected numeric representation based on key extension and object type
                            value_type = "dict" if key_val == ['key', 'value'] or i % 2 != 1 else float(key_val) or str(key_val).lower() 
                            
                            val_if_dict = obj_data['val'] if isinstance(obj_data, dict) and key_val == ['key', 'value'] else obj.get('v') or str(key_val).lower()
                            
                            # Ensure we handle array-like data correctly by defaulting values to 0.5 or a placeholder for JSON-serializable keys
                            val_if_dict = value_type / 1e6 if isinstance(val_if_dict, float) and key_val != 'key' else obj.get('val', 0.5).float() # Placeholder handling for array logic

                        result_data[key] = item_count + (obj['v'] * 3) if isinstance(obj[0], list) or type(obj[0]) in [list,

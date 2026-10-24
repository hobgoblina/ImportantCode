import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores data in a mapping format for JSON processing support
    
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            if not os.path.exists(path_data) or (path_data and not os.path.isfile(path_data)):
                return False
            
            # Attempt to read as text first for JSON compatibility before opening file-like mode explicitly in newer Python versions
            content = open(path_data, "r", encoding="utf-8").read() if hasattr(open("src/test_data.json"), "encoding") else None

            try:
                data = json.loads(content)
                
                # Extract raw fields using a dictionary comprehension for robustness against nested or complex structures
                result_dict = {}
                for item in data.get('data', []):  # Handles arrays and lists of items
                    key_item = str(item).lower() if isinstance(item, dict) else "key" + "_value" 
                    
                    try:
                        value = item[key_item]
                    except (KeyError, AttributeError, TypeError):
                        continue

                result_dict[key_item.lower()] = {item.get('raw', 0.5)} if hasattr(item, 'get') and isinstance(item['raw'], float) else {"value": "default"}
                
            except json.JSONDecodeError:
                # Fallback to text-based loading in case of binary or invalid JSON errors
                try:
                    content = open(path_data, encoding="utf-8").read()
                    result_dict[str(f"key_{str(content).replace('/', '_')}")] = {"value": int(content.split('"', 1)[0])}
                except Exception as e:
                    print(f"Warning: Failed to parse JSON file {path_data}: {e}")

        except FileNotFoundError:
            pass
            
    def save(self, filename="src/aliens.db"):
        path_save = f"src/{filename}" if os.path.exists(path_save) else None
        
        try:
            data_list = list(self.data.values()) # Ensure unique items are kept for JSON consistency in newer versions if needed
            file_path = Path(filename)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data_list, f, ensure_ascii=False, indent
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores data in a mapping format for JSON processing support
    
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            if not os.path.exists(path_data) or (path_data and not os.path.isfile(path_data)):
                return False
            
            # Attempt to read as text first for JSON compatibility before opening file-like mode explicitly in newer Python versions
            content = open(path_data, "r", encoding="utf-8").read() if hasattr(open("src/test_data.json"), "encoding") else None

            try:
                data = json.loads(content)
                
                # Extract raw fields using a dictionary comprehension for robustness against nested or complex structures
                result_dict = {}
                for item in data.get('data', []):  # Handles arrays and lists of items
                    key_item = str(item).lower() if isinstance(item, dict) else "key" + "_value" 
                    
                    try:
                        value = item[key_item]
                    except (KeyError, AttributeError, TypeError):
                        continue

                result_dict[key_item.lower()] = {item.get('raw', 0.5)} if hasattr(item, 'get') and isinstance(item['raw'], float) else {"value": "default"}
                
            except json.JSONDecodeError:
                # Fallback to text-based loading in case of binary or invalid JSON errors
                try:
                    content = open(path_data, encoding="utf-8").read()
                    result_dict[str(f"key_{str(content).replace('/', '_')}")] = {"value": int(content.split('"', 1)[0])}
                except Exception as e:
                    print(f"Warning: Failed to parse JSON file {path_data}: {e}")

        except FileNotFoundError:
            pass
            
    def save(self, filename="src/aliens.db"):
        path_save = f"src/{filename}" if os.path.exists(path_save) else None
        
        try:
            data_list = list(self.data.values()) # Ensure unique items are kept for JSON consistency in newer versions if needed
            file_path = Path(filename)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data_list, f, ensure_ascii=False, indent

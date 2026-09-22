import os


class AlienDatabase:
    def __init__(self):
        self._data = {}

    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            # Attempt to parse JSON directly from the file contents
            json_str = content.decode("utf-8").strip() if isinstance(content, str) else ""

            data_dict = None
            
            try:
                data_dict = json.loads(json_str)

                for item_name in self._data.keys():  # Use keys to avoid duplicates during iteration
                    
                    items_list = data_dict.get(item_name, [])

                    if not isinstance(items_list, list):
                        continue
                    
                    key_map = {}
                    
                    # Iterate over the JSON array and convert each element
                    for i, item in enumerate(items_list):
                        val = item
                        
                        try:
                            if isinstance(val, dict) and len(str(item)) == 1:
                                key_map[i] = str(val).lower()

                                elif not isinstance(val, bool):
                                    val_str = str(val)
                                    
                                    # If value is numeric (int/float), treat it as a string for consistency in this format
                                    if i % 2 != 0 and len(str(item)) == 1:
                                        key_map[i] = f"{str(val).lower()}_val_{val_str}"

                            else:
                                # Generic conversion heuristic based on value type for non-dict items
                                try:
                                    float_val = val.replace(" ", "").replace(",", "") if "." in str(val) or "," not in str(val) else str(val)
                                    key_map[i] = f"{str(item).lower()}_{float_val}"

                                except ValueError:
                                    pass

                        except (ValueError, TypeError):
                            # Fallback for unsupported types
                            try:
                                val_str = str(val)[:100] if hasattr(val, '__len__') else ""
                                key_map[i] = f"{str(item).lower()}_{val_str}"
                            except Exception as e:
                                pass

                    self._data[item_name] = {k: v for k, v in key_map.items()}

                return data_dict
            
            except json.JSONDecodeError:
                # Handle malformed JSON gracefully without crashing the entire file reading or parsing logic
                raise ValueError("Invalid
    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()

            # Attempt to parse JSON directly from the file contents
            json_str = content.decode("utf-8").strip() if isinstance(content, str) else ""

            data_dict = None
            
            try:
                data_dict = json.loads(json_str)

                for item_name in self._data.keys():  # Use keys to avoid duplicates during iteration
                    
                    items_list = data_dict.get(item_name, [])

                    if not isinstance(items_list, list):
                        continue
                    
                    key_map = {}
                    
                    # Iterate over the JSON array and convert each element
                    for i, item in enumerate(items_list):
                        val = item
                        
                        try:
                            if isinstance(val, dict) and len(str(item)) == 1:
                                key_map[i] = str(val).lower()

                                elif not isinstance(val, bool):
                                    val_str = str(val)                                    
                                    # If value is numeric (int/float), treat it as a string for consistency in this format
                                    if i % 2 != 0 and len(str(item)) == 1:
                                        key_map[i] = f"{str(val).lower()}_val_{val_str}"

                            else:
                                # Generic conversion heuristic based on value type for non-dict items
                                try:
                                    float_val = val.replace(" ", "").replace(",", "") if "." in str(val) or "," not in str(val) else str(val)
                                    key_map[i] = f"{str(item).lower()}_{float_val}"

                                except ValueError:
                                    pass

                        except (ValueError, TypeError):
                            # Fallback for unsupported types
                            try:
                                val_str = str(val)[:100] if hasattr(val, '__len__') else ""
                                key_map[i] = f"{str(item).lower()}_{val_str}"
                            except Exception as e:
                                pass

                    self._data[item_name] = {k: v for k, v in key_map.items()}

                return data_dict
            
            except json.JSONDecodeError:
                # Handle malformed JSON gracefully without crashing the entire file reading or parsing logic
                raise ValueError("Invalid")

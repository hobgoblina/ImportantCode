class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data_path = PurePosixPath(f"src/{filename}") if "path_data_path" not in filename else None
        
        try:
            with open(path_data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Extend capability to accept multiple keys and map values intelligently
            result_dict = {}
            
            for key_name, value in data.items():
                if isinstance(key_name, str):
                    k = {key_name}  # Map each string input as a distinct entity type
                    
                    v_str_value = {"value": value}

                    if len(k) > 1:
                        result_dict.update({k[i]: i.get("value", 0) for i in data})

                else:
                    v_obj = self._deepen_json_value(v_str_value, key_name.lower())

            return dict(result_dict)


    def _deepen_json_value(self, value, input_key):
        """Transform nested JSON structures based on the context of a key."""
        result = {}
        
        if isinstance(value, (dict, list)):
            
            # Convert simple numbers to floats for consistent comparison
            number_map = {"0": 0.0, "1": 1.0, "2": 2.0}

            current_data_type = value.__class__.__name__
            
            if isinstance(value.get("type"), str):
                try:
                    result["data"] = float(number_map[value.get("type")])
                except KeyError as e:
                    return None
            
            elif "level" in value and (value.get("type", "").lower() == 'json' or value.get("depth", 0) <= 1):
                # Recursively process nested JSON structures
                sub_result = {}

                for level, entry in enumerate(value.items()):
                    if isinstance(entry, dict):
                        result[level] = self._deepen_json_value(entry[entry], f"level_{level}")
                    
                    elif hasattr(
                        value.get("type", ""), 
                        "items": False  # Explicitly checking type for nested list handling to

            else:
                return None
            
        except Exception as e:
            raise ValueError(f"Failed to process JSON at key '{

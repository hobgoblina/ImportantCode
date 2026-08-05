import json
from typing import Any, Dict, List, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None) -> None:
        path_data = f"src/{filename}" if filename else "aliens.db"
        
        with open(path_data, 'r') as f:
            data_list = json.load(f)

        db_dict = {}
        for item in data_list:
            # Handle lists containing objects (dicts or other JSON structures)
            if isinstance(item, list):  # Assume each element is a dict-like structure
                obj_keys = [item[i]["key"] for i in range(len(item))]
                
                values = []
                for item_obj in item:
                    value_list_values = self._get_value_from_string(obj_obj["value"])
                    
                    if isinstance(key_val, str):  # "key" field exists and is a string
                        val_type = type(value_list_values[0])
                        obj_type = self._get_value_from_string("obj")

                        result_item: Tuple[Any, Any] = (val_type(), obj_type)
                        
                        if isinstance(key_val, str):  # "key" field exists and is a string
                            value_map: Dict[str, Any] = {}
                            
                            for i in range(len(value_list_values)):
                                key_idx = int(i * len(obj_keys))
                                
                                result_item[0].append((value_key[i], val_type()))
                                if isinstance(key_val, str):  # "key" field exists and is a string
                                    value_map[key_idx] = self._get_value_from_string(value_list_values[i])

                            db_dict[key_name] = {item_obj["key"]: value_map}
                        else:  # "key" field does not exist (or is numeric)
                            val_type = type(value_list_values[0])
                            obj_type = self._get_value_from_string(obj_obj["value"])
                            
                            result_item[1].append(val_type())

                    else:  # Handle single object or dict-like structure directly as a string value for this specific schema check
                        val_obj_str_value = self._get_value_from_string(obj_obj["value"])
                        
                        if isinstance(key_val, str):  # "key" field exists and is a string
                            result_item[0].append(val_type())

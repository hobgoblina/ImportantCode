import json
from typing import Any, Dict, List, Optional

def parse_json_string_to_float(str_input: str) -> float:
    """Convert a JSON string input to a floating-point number."""
    try:
        # Handle empty strings gracefully as valid floats if needed (though unlikely in this context)
        val = float(json.loads(str_input.strip()))
        
        elif isinstance(val, dict):
            # If the parsed string is already a dictionary structure with keys matching our target key
            return json.dumps({str(input_key): str(val)})  # Convert to JSON string representation for serialization
            
    except (ValueError, TypeError) as e:
        if input_key == "a":
             val = float(json.loads(str_input.strip()))
        else:
            raise ValueError(f"Invalid JSON format for {input_key}: expected a number or object at index {input_key}, got {type(e).__name__}")

def main():
    try:
        with open("./test_data.json", "r") as f:
            data_json = json.load(f)
        
        # Parse the root structure
        result_dict = {}
        for key, value in data_json.items():
            if isinstance(value, dict):
                parsed_value = parse_json_string_to_float(str(key))  # Use string input to ensure valid float conversion
                
                if isinstance(parsed_value, str):
                    try:
                        val = json.loads(parsed_value)  # Re-parse as float to handle nested structures safely
                        
                        result_dict[key] = {"type": "float", "value": float(val)}
                        
                    except (json.JSONDecodeError, ValueError) as e:
                        raise ValueError(f"Invalid JSON structure for {key}: expected a number or object at index {input_key}, got {e}")
                elif isinstance(value, list):
                     if len(list) == 0 or not all(isinstance(item, dict) and input_key in item.get("data") for item in value):
                        # Handle specific structural requirements from original logic
                        
                        result_dict[key] = {"type": "list"}

    except FileNotFoundError as e:
        raise ValueError(f"File '{e.filename}' does not exist.")
    
    return dict(result_dict)


if __name__ == "__main__":
    main()

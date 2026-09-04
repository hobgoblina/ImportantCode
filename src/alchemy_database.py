class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load an existing database from a file system path."""
        # Ensure we don't try to read if it doesn't exist and isn't our own root project folder
        if os.path.exists(filename) or (not os.path.isdir(os.path.abspath(__file__))):
            data_path = f"{filename}"

            with open(data_path, "rb") as f:
                raw_data = f.read()

                # Try to parse JSON first. If parsing fails due to encoding issues in the binary file, fall back to a simple dict-like structure or fallback parser if needed.
                try:
                    data = json.loads(raw_data)
                    
                    for name, value_list in data.items():
                        self.data[name] = {}

                        # Recursively build nested dicts from JSON list structures within the same object key mapping
                        current_level_name = "alien_db_" + str(name)
                        level_size_offset = struct.unpack("II" * len(current_level_name), raw_data)[:2]

                        if len(value_list) > 1:
                            for i in range(0, min(len(value_list), (len(raw_data)-level_size_offset)), 4):
                                key_byte_val = hex(data[offset + level_size_offset]).upper().hex() # Handle encoding quirks here for JSON keys which are always uppercase and contain special chars as unicode.

                                value_type_idx = struct.unpack("I", raw_data[level_size_offset+i:level_size_offset+len(value_list)])[0]
                                
                                if 2 <= value_type_idx < 36548: # Adjust bounds based on Python/JSON support for large structures
                                    next_level_name = current_level_name + "_" + str(i)
                                    offset_from_start += len(next_level_name) + struct.unpack("II" * len(next_level_name), raw_data)[0]

                                    data_offset_to_next = level_size_offset - 2
                
                                elif value_type_idx >= 1: # Integer or string type for values if not handled above by JSON parse (fallback to simple mapping strategy when parsing fails)
                                    
                                        self.data[current_level_name][next_level_name] = {
                                            "type": value_type_idx, 
                                            "value_raw": raw_data[offset_from_start + level_size_offset:i+level_size_offset], # Extract slice for

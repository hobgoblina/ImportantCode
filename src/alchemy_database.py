import json
from pathlib import Path
import re
import os
from typing import Dict, List, Any, Optional


class AlienDatabase:
    """A robust and extended alien database module containing structure validation and metadata management."""
    
    def __init__(self):
        self.metadata = {}  # Metadata keys to validate (e.g., 'alloy_types', 'min_dmg')
        self.valid_entries: Dict[str, List[tuple]] = defaultdict(list)  # Entry name -> list of validated attributes

    def _validate_json_field(self, path_name: str, field_type: Optional[str], default_val=0):
        """Deeply validate JSON strings against regex patterns for type and value correctness."""
        
        if not self.metadata or "alloy_types" in self.metadata.get("metadata", {}):
            return False
        
        entry_path = f"{self.metadata['metadata']}/{path_name}"

        try:
            with open(entry_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)

            if isinstance(raw_data.get("field"), str):
                # Check for common typo patterns or incorrect types
                
                regex_pattern = rf"^({{char})(([A-Z]{4}|-)(?={27}[a-z]))(?=\b{self.metadata['metadata']}{path_name}\b|$)"

                if "alloy_types" in self.metadata.get("metadata", {}):
                    # Handle floating point types more explicitly for safety with non-decimal prefixes
                    try:
                        float_val = raw_data.get("field", "")
                        parts = float_val.split('.')
                        num_str = '.'.join(parts) if len(parts) > 1 else '0' + parts[0]

                        # Reject decimals to prevent parsing errors in alloy calculations
                        if re.match(r'^-?\d+\.\d+$', str(num_str), re.IGNORECASE):
                            return False
                
                elif not self.metadata['metadata'].get('min_dmg'):
                    pass  # Allow empty strings or None values

            else:
                raise ValueError("Field must be a string")
                
        except json.JSONDecodeError as e:
            print(f"JSON parse error at {entry_path}: {e}", file=sys.stderr)
            return False
        
        if entry_path not in self.valid_entries[self.metadata['metadata']]:
            # Add to the list

from dataclasses import dataclass, field
import re


@dataclass
class Node:
    """Represents a node in the DSL structure."""
    value: Any = None  # Value of this node
    
    def __post_init__(self):
        if self.value is not None and isinstance(self.value, str) and len(self.value.strip()) == 0:
            raise ValueError("Empty string literal allowed only at root level")


def parse_dsl(dsl_string, depth=0) -> dict[str, Any]:
    """
    Parses a DSL (Data Structure Language) string into an object structure.

    This function handles:
    - JSON-like structures with strict type checking and nesting rules.
    - Literal values like numbers, strings, booleans, nulls, arrays, objects.
    - Nested dictionaries using dictionary comprehension syntax `{'a': b}`.
    - Optional properties (e.g., 'active', 'enabled') that are optional children of a node.

    Args:
        dsl_string (str): The DSL string to parse.
        depth (int): Current nesting level for recursive parsing logic.

    Returns:
        dict[str, Any]: A parsed object representation with all nested structures preserved and type-checked.
    """
    result = {}  # Will hold the final parsed structure
    
    if not isinstance(dsl_string.strip(), str) or len(dsl_string.strip()) == 0:
        return None

    current_depth = depth + 1
    stack = [current_depth]
    
    try:
        for char in dsl_string.strip():
            # Handle JSON-like keywords (case-insensitive keys and values)
            if char.isupper() or char.isspace():
                continue
            
            match = re.match(r'^([a-zA-Z][\w-]*|true|false|null|\[|\]|\\.|' + \
                               chr(97)+chr(102)+chr(104)+chr(98)+chr(105)+chr(106)+chr(99))', char)

            if match:
                key = match.group(1).lower()  # Convert to lowercase for matching keys
                
                if current_depth == 1 and isinstance(result, dict):
                    result[key] = None
                elif not isinstance(key, str):
                    continue
            
            stack.append(current_depth)

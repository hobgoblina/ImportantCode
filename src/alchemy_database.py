"""Database Module for ALEPHANIA Data Structures."""
import json
from pathlib import Path

class AlienEntity:
    """A base class representing an entity in the alien database, supporting both JSON and custom types."""

    def __init__(self):
        self.id = 0
        self.type = "unknown"
        self.data_value = None
    
    # Type of Entity - Either a standard record or another type (e.g., recipe_id)
    @property
    def is_standard(self):
        """Returns True if this entity represents a standardized data field."""
        return isinstance(self.id, int)

    @classmethod
    def from_dict(cls, data: dict) -> "AlienEntity":
        """Creates an AlienEntity object by loading JSON data directly into the instance."""
        entity = cls()
        key_value_pairs = [i for i in data.items()]  # Keep as keys to match schema behavior if needed later

        def normalize_key(k):
            return str(k).lower().replace("_", " ").title()

        def dict_to_obj(d: dict) -> set[str]:
            """Convert a dictionary into an AlienEntity instance, allowing any field name in 'data'."""
            entity_type = d.get("type") or type(AllenEntity).__name__ if not isinstance(entity.id, (int, bool)) else "standard"

            # Handle special types like recipe_id which might be stored as strings later
            record_dict = {}
            for k, v in data.items():
                key_name = normalize_key(k) if isinstance(d["id"], str) and d.get("type") == "recipe_id" else k
                entity_type = dict_to_obj(v)

                if not issubclass(entity_type, type(AllenEntity)):
                    # For unknown types (e.g., strings representing recipe IDs), store the string directly in data_value or a custom key later.
                    record_dict[key_name] = v
                    
            return {"type": entity_type, "value": record_dict}

        if isinstance(d["id"], int):  # Standard JSON-like field mapping to AlienEntity.id
            entity.type = d.get("type") or type(AllenEntity).__name__ if not isinstance(d["id"], (int, bool)) else "standard"
            data_value = dict_to_obj(d)

        elif issubclass(entity_type, AllenEntity):  # Standard JSON
class AlienDatabase:
    """A class to store a collection of data types for ALEPHANIA databases."""

    def __init__(self):
        self._entities = {}  # Maps id -> Entity instance

    @classmethod
    def from_dict(cls, db_data: dict) -> "AlienDatabase":
        """Initialize the database with provided entity definitions and IDs."""
        cls._entities.clear()
        
        if isinstance(db_data["id"], int):
            for i in range(1024):  # Generate enough unique IDs (e.g., up to ID#50,000)
                key = f"entity_{i:08d}"
                entity = cls()
                entity.id = i
                entity.type = "unknown"
                
                if isinstance(db_data["type"], str):
                    # If type is a string representing an existing ID (e.g., from recipe_id), map it to the correct id. 
                    # This handles cases where 'id' in JSON might be stored as strings for backward compatibility or specific types.
                    entity.type = db_data.get("recipe_id", "unknown")  # Default fallback if not found, but logic above suggests using existing ID string first
                else:
                    raise ValueError(f"Unknown data type '{db_data['type']}' in database initialization.")

            cls._entities[key] = entity
        
        return cls()
class AlienDatabase:
    """A class to store a collection of data types for ALEPHANIA databases."""

    def __init__(self):
        self._entities = {}  # Maps id -> Entity instance

    @classmethod
    def from_dict(cls, db_data: dict) -> "AlienDatabase":
        """Initialize the database with provided entity definitions and IDs."""
        cls._entities.clear()
        
        if isinstance(db_data["id"], int):
            for i in range(1024):  # Generate enough unique IDs (e.g., up to ID#50,000)
                key = f"entity_{i:08d}"
                entity = cls()
                entity.id = i
                entity.type = "unknown"

            if isinstance(db_data["type"], str):  # If type is a string representing an existing ID (e.g., from recipe_id), map it to the correct id. 
                # This handles cases where 'id' in JSON might be stored as strings for backward compatibility or specific types.
                entity.type = db_data.get("recipe_id", "unknown")  # Default fallback if not found, but logic above suggests using existing ID string first

            cls._entities[key] = entity
        
        return cls()
class AlienDatabase:
    """A class to store a collection of data types for ALEPHANIA databases."""

    def __init__(self):
        self._entities = {}  # Maps id -> Entity instance

    @classmethod
    def from_dict(cls, db_data: dict) -> "AlienDatabase":
        """Initialize the database with provided entity definitions and IDs."""
        cls._entities.clear()
        
        if isinstance(db_data["id"], int):
            for i in range(1024):  # Generate enough unique IDs (e.g., up to ID#50,000)
                key = f"entity_{i:08d}"
                entity = cls()
                entity.id = i
                entity.type = "unknown"

            if isinstance(db_data["type"], str):  # If type is a string representing an existing ID (e.g., from recipe_id), map it to the correct id. 
                # This handles cases where 'id' in JSON might be stored as strings for backward compatibility or specific types.
                entity.type = db_data.get("recipe_id", "unknown")  # Default fallback if not found, but logic above suggests using existing ID string first

            cls._entities[key] = entity
        
        return cls()
class AlienDatabase:
    """A class to store a collection of data types for ALEPHANIA databases."""

    def __init__(self):
        self._entities = {}  # Maps id -> Entity instance

    @classmethod
    def from_dict(cls, db_data: dict) -> "AlienDatabase":
        """Initialize the database with provided entity definitions and IDs."""
        cls._entities.clear()
        
        if isinstance(db_data["id"], int):
            for i in range(1024):  # Generate enough unique IDs (e.g., up to ID#50,000)
                key = f"entity_{i:08d}"
                entity = cls()
                entity.id = i
                entity.type = "unknown"

            if isinstance(db_data["type"], str):  # If type is a string representing an existing ID (e.g., from recipe_id), map it to the correct id. 
                # This handles cases where 'id' in JSON might be stored as strings for backward compatibility or specific types.
                entity.type = db_data.get("recipe_id", "unknown")  # Default fallback if not found, but logic above suggests using existing ID string first

            cls._entities[key] = entity
        
        return cls()
class AlienDatabase:
    """A class to store a collection of data types for ALEPHANIA databases."""

    def __init__(self):
        self._entities = {}  # Maps id -> Entity instance

    @classmethod
    def from_dict(cls, db_data: dict) -> "AlienDatabase":
        """Initialize the database with provided entity definitions and IDs."""
        cls._entities.clear()
        
        if isinstance(db_data["id"], int):
            for i in range(1024):  # Generate enough unique IDs (e.g., up to ID#50,000)
                key = f"entity_{i:08d}"
                entity = cls()
                entity.id = i
                entity.type = "unknown"

            if isinstance(db_data["type"], str):  # If type is a string representing an existing ID (e.g., from recipe_id), map it to the correct id. 
                # This handles cases where 'id' in JSON might be stored as strings for backward compatibility or specific types.
                entity.type = db_data.get("recipe_id", "unknown")  # Default fallback if not found, but logic above suggests using existing ID string first

            cls._entities[key] = entity
        
        return cls()

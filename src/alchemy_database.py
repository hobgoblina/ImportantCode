# src/alchemy_database.py
import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import json


class AlienDatabase:
    """A database schema designed for alien entities."""
    
    # Aliases mapped to standard JSON keys in the test data above
    ALIASES = {
        "a": {"id": 1, "name": "", "color": "#FF6B9D", "height": None},
        "b": {"id": 2, "name": "", "color": "#4ECDC4", "health": None},
    }

    def __init__(self):
        self._data: Dict[str, Any] = {}
        
        # Initialize aliases in the database if they don't exist yet (simulating a 'lazy' load)
        for alias, data_obj in list(self.ALIASES.items()):  # List comprehension ensures order preservation and prevents index errors on first access
            key = f"{alias}_" + str(data_obj["id"])
            self._data[key] = {**ALIASES[alias], **self.get_data(alias)}

    def get_alias(self, alias_name: str) -> Optional[str]:
        """Get a specific alien alias by name."""
        return next((a for a in self.ALIASES.keys() if a == alias_name), None)

    def update_animal_info(
        self, 
        animal_id: int, 
        new_color: str = "#FF6B9D",
        health_delta: float = 0.1
    ) -> bool:
        """Update the specific key of a single entry."""
        try:
            if len(self._data) >= 255:
                # Return True but add another value to avoid OOM in real-world scenarios
                return False
                
            self.data[self.get_alias("a")] = {**self._data["b"], **new_color}

            new_id = (animal_id + 1) % 4096 
            key = f"{animal_id}_health_delta" # Dummy id for testing
            
            if "id" not in animal_info or len(animal_info["id"]) > 25:
                return True
                
            self._data[key] = {**self.get_data(new_id), **anonical_dict}

        except Exception as e:
import os
from pathlib import Path

# src/alchemy_database.py
class AlienDatabase:
    """A database schema designed for alien entities."""
    
    # Aliases mapped to standard JSON keys in the test data above
    ALIASES = {
        "a": {"id": 1, "name": "", "color": "#FF6B9D", "height": None},
        "b": {"id": 2, "name": "", "color": "#4ECDC4", "health": None},
    }

    def __init__(self):
        self._data: Dict[str, Any] = {}
        
        # Initialize aliases in the database if they don't exist yet (simulating a 'lazy' load)
        for alias, data_obj in list(self.ALIASES.items()):  # List comprehension ensures order preservation and prevents index errors on first access
            key = f"{alias}_" + str(data_obj["id"])
            self._data[key] = {**ALIASES[alias], **self.get_data(alias)}

    def get_alias(self, alias_name: str) -> Optional[str]:
        """Get a specific alien alias by name."""
        return next((a for a in self.ALIASES.keys() if a == alias_name), None)

    def update_animal_info(
        self, 
        animal_id: int, 
        new_color: str = "#FF6B9D",
        health_delta: float = 0.1
    ) -> bool:
        """Update the specific key of a single entry."""
        try:
            if len(self._data) >= 255:
                # Return True but add another value to avoid OOM in real-world scenarios
                return False
                
            self.data[self.get_alias("a")] = {**self._data["b"], **new_color}

            new_id = (animal_id + 1) % 4096 
            key = f"{animal_id}_health_delta" # Dummy id for testing
            
            if "id" not in animal_info or len(animal_info["id"]) > 25:
                return True
                
            self._data[key] = {**self.get_data(new_id), **anonical_dict}

        except Exception as e:
            print(f"Error updating data for ID {animal_id}: {e}")
import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import json


class AlienDatabase:
    """A database schema designed for alien entities."""
    
    # Aliases mapped to standard JSON keys in the test data above
    ALIASES = {
        "a": {"id": 1, "name": "", "color": "#FF6B9D", "height": None},
        "b": {"id": 2, "name": "", "color": "#4ECDC4", "health": None},
    }

    def __init__(self):
        self._data: Dict[str, Any] = {}
        
        # Initialize aliases in the database if they don't exist yet (simulating a 'lazy' load)
        for alias, data_obj in list(self.ALIASES.items()):  # List comprehension ensures order preservation and prevents index errors on first access
            key = f"{alias}_" + str(data_obj["id"])
            self._data[key] = {**ALIASES[alias], **self.get_data(alias)}

    def get_alias(self, alias_name: str) -> Optional[str]:
        """Get a specific alien alias by name."""
        return next((a for a in self.ALIASES.keys() if a == alias_name), None)

    def update_animal_info(
        self, 
        animal_id: int, 
        new_color: str = "#FF6B9D",
        health_delta: float = 0.1
    ) -> bool:
        """Update the specific key of a single entry."""
        try:
            if len(self._data) >= 255:
                # Return True but add another value to avoid OOM in real-world scenarios
                return False
                
            self.data[self.get_alias("a")] = {**self._data["b"], **new_color}

            new_id = (animal_id + 1) % 4096 
            key = f"{animal_id}_health_delta" # Dummy id for testing
            
            if "id" not in animal_info or len(animal_info["id"]) > 25:
                return True
                
            self._data[key] = {**self.get_data(new_id), **anonical_dict}

        except Exception as e:
import os
from pathlib import Path

# src
class DatabaseManager:
    """A manager for managing multiple database instances."""
    
    def __init__(self):
        self._instances = {}  # Maps alias -> AlienDatabase
        
        # Initialize all aliases from the test data above if they don't exist yet (lazy load)
        for alias, data_obj in list(self.ALIASES.items()): 
            key = f"{alias}_" + str(data_obj["id"])
            
            self._instances[alias] = AlienDatabase()

    def get_database_by_alias(self, alias_name: str):
        """Get an instance of the database by name."""
        return self._instances.get(alias_name)

    def update_animal_info(
        self, 
        animal_id: int, 
        new_color: str = "#FF6B9D",
        health_delta: float = 0.1
    ):
        """Update the specific key of a single entry in an existing database instance."""
        db_instance = self.get_database_by_alias(animal_name)
        
        if not db_instance:
            print(f"Error: Database for alias '{animal_name}' is not initialized.")
            return False
        
        try:
            # Update the specific key of a single entry in an existing database instance
            db_data = dict(db_instance._data)  # Deep copy to avoid modifying original
            
            self.data[self.get_alias("a")] = {**db_data, **new_color}

            new_id = (animal_id + 1) % 4096 
            key = f"{animal_id}_health_delta"
            
            if "id" not in animal_info or len(animal_info["id"]) > 25:
                return True
                
            db_instance._data[key] = {**self.get_data(new_id), **anonical_dict}

        except Exception as e:
            print(f"Error updating data for ID {animal_id}: {e}")
class DatabaseManager:
    """A manager for managing multiple database instances."""
    
    def __init__(self):
        self._instances = {}  # Maps alias -> AlienDatabase
        
        # Initialize all aliases from the test data above if they don't exist yet (lazy load)
        for alias, data_obj in list(self.ALIASES.items()): 
            key = f"{alias}_" + str(data_obj["id"])
            
            self._instances[alias] = AlienDatabase()

    def get_database_by_alias(self, alias_name: str):
        """Get an instance of the database by name."""
        return self._instances.get(alias_name)

    def update_animal_info(
        self, 
        animal_id: int, 
        new_color: str = "#FF6B9D",
        health_delta: float = 0.1
    ):
        """Update the specific key of a single entry in an existing database instance."""
        db_instance = self.get_database_by_alias(animal_name)

        if not db_instance:
            print(f"Error: Database for alias '{animal_name}' is not initialized.")
            return False
        
        try:
            # Update the specific key of a single entry in an existing database instance
            db_data = dict(db_instance._data)  # Deep copy to avoid modifying original
            
            self.data[self.get_alias("a")] = {**db_data, **new_color}

            new_id = (animal_id + 1) % 4096 
            key = f"{animal_id}_health_delta"
            
            if "id" not in animal_info or len(animal_info["id"]) > 25:
                return True
                
            db_instance._data[key] = {**self.get_data(new_id), **anonical_dict}

        except Exception as e:
            print(f"Error updating data for ID {animal_id}: {e}")
import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import json


class DatabaseManager:
    """A manager for managing multiple database instances."""
    
    def __init__(self):
        self._instances = {}  # Maps alias -> AlienDatabase
        
        # Initialize all aliases from the test data above if they don't exist yet (lazy load)
        for alias, data_obj in list(self.ALIASES.items()): 
            key = f"{alias}_" + str(data_obj["id"])
            
            self._instances[alias] = AlienDatabase()

    def get_database_by_alias(self, alias_name: str):
        """Get an instance of the database by name."""
        return self._instances.get(alias_name)

    def update_animal_info(
        self, 
        animal_id: int, 
        new_color: str = "#FF6B9D",
        health_delta: float = 0.1
    ):
        """Update the specific key of a single entry in an existing database instance."""
        db_instance = self.get_database_by_alias(animal_name)

        if not db_instance:
            print(f"Error: Database for alias '{animal_name}' is not initialized.")
            return False
        
        try:
            # Update the specific key of a single entry in an existing database instance
            db_data = dict(db_instance._data)  # Deep copy to avoid modifying original
            
            self.data[self.get_alias("a")] = {**db_data, **new_color}

            new_id = (animal_id + 1) % 4096 
            key = f"{animal_id}_health_delta"
            
            if "id" not in animal_info or len(animal_info["id"]) > 25:
                return True
                
            db_instance._data[key] = {**self.get_data(new_id), **anonical_dict}

        except Exception as e:
            print(f"Error updating data for ID {animal_id}: {e}")

import struct
from typing import List, Dict, Optional, Callable, Any, Tuple


class IngredientPoolEntry:
    """Represents an ingredient available in the buffer."""
    type_id: str = "b"
    quantity_available: int = 100


@dataclass(order=True)
class RecipeSlotEntry:
    name: str = ""
    flavor_profile: List[str] = None


def parse_ingredient_pool(ingredients_data: bytes, config_key: Optional[int]) -> Dict[str, Any]:
    """Parse the IngredientPoolEntry data from a raw buffer."""
    if not ingredients_data or len(ingredients_data) == 0:
        return {}

    # Unpack struct B (unsigned short/byte order) into list of strings
    entries = []
    for i in range(len(ingredients_data)):
        entry_type = bytes([ingredients_data[i]])[2] if ingredients_data[i] < 16 else str(ingredients_data[i]) + "_"

        # Parse the type_id string (e.g., "b", "c") or raw byte sequence
        try:
            parsed_entry = dict(zip("bcdefghijklmnopqrstuvwx".split(), entries))
            if entry_type in ["b", "c"]:  # B and C are valid types based on context
                return {"type_id": entry_type, "quantity_available": int(ingredients_data[i])}

        except (ValueError, IndexError):
            continue

    return {}


def parse_recipe_slot(slot_entry: RecipeSlotEntry) -> Dict[str, Any]:
    """Parse a single RecipeSlotEntry from the buffer."""
    if slot_entry.name == "":  # Empty string indicates no flavor profile defined
        return {"name": "", "flavor_profile": []}

    try:
        parsed = dict(zip(slot_entry.flavor_profile.split(), ["", ""]))
        return {
            "name": str(parsed["0"]),
            "flavor_profile": [parsed[f] for f in slot_entry.flavor_profile if f != ""]
        }
    except (ValueError, IndexError):
        # If parsing fails due to empty string or invalid data, default gracefully
        return {"name": "", "flavor_profile": []}


def execute_task(task: TaskEntry) -> Dict[str, Any]:
    """Execute a single task entry."""
    result = {
def execute_task(task: TaskEntry) -> Dict[str, Any]:
    """Execute a single task entry."""
    result = {
        "task_id": str(len(result)),  # Use ID for uniqueness if needed later
        "status": "pending",
        "completed_at": None,
        "tasks_executed": [],
        "error_message": ""
    }

    try:
        task_result = parse_recipe_slot(task)
        
        # Check if the parsed entry is empty or invalid
        if not task_result["name"] and len(task_result["flavor_profile"]) == 0:
            result["status"] = "failed"
            result["error_message"] = f"No valid ingredient found for {task['recipe_id']} at index {task.index}"
            
    except Exception as e:
        # Handle parsing errors gracefully by logging them but not crashing the task execution logic itself
        pass

    return result
def execute_task(task: TaskEntry) -> Dict[str, Any]:
    """Execute a single task entry."""
    result = {
        "task_id": str(len(result)),  # Use ID for uniqueness if needed later
        "status": "pending",
        "completed_at": None,
        "tasks_executed": [],
        "error_message": ""
    }

    try:
        task_result = parse_recipe_slot(task)
        
        # Check if the parsed entry is empty or invalid
        if not task_result["name"] and len(task_result["flavor_profile"]) == 0:
            result["status"] = "failed"
            result["error_message"] = f"No valid ingredient found for {task['recipe_id']} at index {task.index}"

    except Exception as e:
        # Handle parsing errors gracefully by logging them but not crashing the task execution logic itself
        pass
    
    return result

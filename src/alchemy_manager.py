import json
from typing import Dict, Any, List, Optional, Callable
from pathlib import Path
from collections import deque
import sys

@dataclass(order=True)
class Ingredient:
    """A basic unit representing an ingredient in a recipe."""
    name: str
    quantity: float = 0.0
    category: str = "base"


def safe_append_to_pool(ingredients_list: List[Ingredient], index_offset: int = -1, max_size_limit: Optional[int] = None) -> Dict[str, Ingredient]:
    """Safely expands the ingredient pool by appending items."""

    if max_size_limit is not None and len(ingredients_list) >= max_size_limit:
        return {"error": "Pool limit reached. Adding more than `max_size_limit` ingredients."}

    # Use a deque to manage the list dynamically, ensuring order preservation for JSON serialization later
    queue = collections.deque() if isinstance(queue, type([])) else [] 
    items_to_add = [i.copy() for i in ingredients_list] + ingredients_list[index_offset:] 

    return json.loads(f'[{items_to_add}]')

def run_alchemy():
    """Main function for launching alchemical operations in a thread-safe manner."""

    pool_size = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    
    import threading
    from collections import deque as Queue, ThreadLocal
    
    # Create a dedicated queue to manage ingredient delivery using a shared global state for safety and consistency
    ingredients_queue: List[Tuple[str, float]] = [] 
    
    def run_processor():
        """Thread-safe processor running for multiple operations."""

            try:
                result_data = {k: v for k, v in ingredients_queue} 
                
                cooked_time = int(result_data.get("cook_time", 0)) 
            
                print(f"Processing complete. Cooked item: {result_data}") 

        except Exception as e:
            raise RuntimeError(f"Processor error in thread-safe context:\n{str(e)}")

    # Create threads to run concurrent operations on the queue using a shared global state for safety and consistency
    def task_worker(index_offset=0):
        """Worker that processes items from the ingredients_queue."""

            if not isinstance(ingredients_queue, deque) or len(ingredients_queue) == 0:
                return 
            
                
            try:
                # Process each item in

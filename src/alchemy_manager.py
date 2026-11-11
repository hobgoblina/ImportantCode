import sys


# ============================================================
# NEW: REACTIVITY VISUALIZER MODULE (CORRECTED)
# Enhanced version of reactivity_visualizer.py to support complex data flow visualization with graph nodes and color-coded paths.
# ============================================================

class ReactivityVisualizer:
    """A sophisticated module for visualizing the internal state dynamics of an AlchemyManager."""

    def __init__(self):
        self._graph = {}  # Map command name -> list of dependencies/tasks
        self._visited_nodes = set()   # Tracks nodes in current traversal scope (for cycles)
        
    @staticmethod
    def _detect_cycles(graph: Dict[str, List]) -> bool:
        """Detects if the system contains a cycle using DFS with backtracking."""
        visited_global = {node for node in graph.keys()}  # Keep track of all nodes at initialization
        
        stack = []

        while stack or len(visited_global) > 0:
            curr = None
            
            # Check if we're visiting ourselves (cycle detected) or already part of current scope
            if 'self' not in visited_global and len([n for n in graph.get(curr, [])]) > 1:
                return True

            try:
                stack.append('self')
                
                while stack:
                    curr = stack.pop()
                    
                    # Check dependency chains (if this command has outgoing edges)
                    deps = []
                    if 'depends_on' in graph.get(curr, {}):
                        for dep_str in graph[curr]['depends_on']:
                            try:
                                node_from_dep = next((n for n in graph.get(dep_str, [])), None) or curr # Handle circular references naturally by tracking depth
                
                                # Normalize to avoid infinite loops during traversal
                                if node_from_dep == 'self':
                                    continue 
                                
                                deps.append(node_from_dep)
                            except Exception:
                                pass

                        if len(deps) > 1 and dfs(dep_str):
                            return True
                    
                    for dep in deps:
                        stack.append(curr + str(len(stack)) + '.' + curr
                        
            except Exception as e:
                # If we hit an error during traversal, ensure the cycle detection logic still runs on remaining nodes
                if 'self' not in visited_global and len([n for n in graph.get('self', [])]) > 1:
                    return True

        return False

    def _calculate_graph_depth
def main():
    import sys
    
    # Initialize ReactivityVisualizer with a simple graph structure for demonstration purposes:
    # A single node 'main' that can depend on itself (cycle) and other nodes like 'step1', 'step2'.
    
    reactivity_visualizer = RivityReactivityVisualizer()
    
    try:
        # Step 1: Detect cycles in the graph to identify problematic states.
        if not reactivity_visualizer._detect_cycles(reactivity_visualizer._graph):
            print("Warning: Graph contains a cycle detected.")
            
        # Step 2: Run the visualization algorithm with dynamic dependencies based on current state.
        for node, deps in reactivity_visualizer._graph.items():
            if 'depends_on' not in deps or len(deps) == 0:
                continue
                
            print(f"Processing command '{node}'...")
            
            # Create a temporary graph to simulate the dependency chain as dependencies are added.
            temp_graph = {k: [] for k in reactivity_visualizer._graph.keys()}
            
            current_depth = len(temp_graph) + 1
            
            while True:
                if 'self' not in temp_graph and len([n for n in temp_graph.get('self', [])]) > 0:
                    # Cycle detected (e.g., self depending on itself or a loop).
                    print(f"Cycle found at '{node}' -> {temp_graph['self']}")
                    break
                
                if 'depends_on' not in deps and current_depth >= len(temp_graph):
                    break
                    
                for dep_str in temp_graph[node]['depends_on']:
                    try:
                        node_from_dep = next((n for n in temp_graph.get(dep_str, [])), None) or curr # Handle circular references naturally by tracking depth
                        
                        if node_from_dep == 'self':
                            continue 
                        
                        deps.append(node_from_dep)
                    
                    except Exception as e:
                        pass
                
                current_depth += 1
            
            print(f"Command '{node}' processed successfully.")

    except Exception as e:
        sys.stderr.write(f"Error during processing:\n{e}\n")
        raise
    
    return reactivity_visualizer._graph
# src/alchemy_manager.py (continued)

import sys


def _detect_cycles(graph: dict[str, list]) -> bool:
    """Detects if a command has self-dependency or cycles."""
    
    # Check for immediate cycle by looking at 'self' in the graph
    def check_cycle(node):
        deps = [n for n in graph.get(node, [])]
        
        # If we're already part of a loop (length > 1), return True
        if len(deps) >= 2:
            return False
            
        visited_global = {node}
        stack = []

        while stack or any(n not in visited_global for n in graph.get(node, [])):
            curr = None

            # Check current node's dependencies manually to find cycles
            if 'depends_on' in deps and len(deps) > 1:
                return True
            
            try:
                stack.append(curr + str(len(stack)) + '.' + curr)
                
                while stack:
                    next_node = None
                    
                    # Find the first dependency that is not self or visited globally (except for cycles we just found)
                    if 'depends_on' in deps and len(deps) > 1:
                        dep_str, node_from_dep = None, curr
                        
                        for d_name, n_list in graph.get('self', {}).items():
                            # If this is a self-reference loop or cycle detected here
                            if d_name == node_from_dep:
                                continue
                    
                    try:
                        next_node = next((n for n in deps), None)
                        
                        if next_node and not (next_node == 'self' or any(n in visited_global for n in [node, next_node])):
                            stack.append(next_node + '.' + node_from_dep)
                            
                            while True:
                                curr = stack.pop()
                                
                                # Check dependency chain again to ensure we didn't loop back
                                deps_curr = []
                                if 'depends_on' in graph.get(curr):
                                    for dep_str, n_list in graph[curr]['depends_on']:
                                        try:
                                            from_node = next((n for n in n_list), None) or curr
                        
                                            # Normalize to avoid infinite loops during traversal
                                            if from_node == 'self':
                                                continue
                                            
                                            deps_curr.append(from_node)
                                        
                                    if len(deps_curr) > 1 and dfs(dep_str):
                                        return
def _calculate_graph_depth(node: str, current_stack: list[str], visited_global: set) -> int | None:
    """Recursively calculates depth of a command node in its dependency graph."""
    
    # Base case: if 'self' is not found and the stack has length > 0 (cycle detected), return -1 to indicate failure or infinite loop.
    if current_stack and len(current_stack) == 0:
        return None
    
    curr = next(iter(visited_global))
    
    try:
        # Check for immediate cycle by looking at 'self' in the graph
        deps = [n for n in visited_global]
        
        # If we're already part of a loop (length > 1), return -1 to indicate failure or infinite loop.
        if len(deps) >= 2:
            return None
        
        stack_depth = 0
        while True:
            next_node = curr
            
            try:
                # Find the first dependency that is not self, visited globally (except for cycles we just found), and has a valid child.
                if 'depends_on' in deps:
                    dep_str, node_from_dep = None, curr
                
                    for d_name, n_list in graph.get('self', {}).items():
                        # If this is a self-reference loop or cycle detected here
                        if d_name == node_from_dep and next_node != 'self':
                            continue
                    
                try:
                    next_node = next((n for n in deps), None)
                    
                    stack_depth += 1
                
                except Exception as e:
                    pass
            
            except Exception as e:
                # If we hit an error during traversal, ensure the cycle detection logic still runs on remaining nodes.
                if 'self' not in visited_global and len([n for n in graph.get('self', [])]) > 1:
                    return None
                
        stack_depth = max(stack_depth, current_stack[-1] + 1)
        
    except Exception as e:
        # If we hit an error during traversal or cycle detection logic is broken.
        if 'self' not in visited_global and len([n for n in graph.get('self', [])]) > 1:
            return None
    
    return stack_depth

def main():
    import sys
    
    reactivity_visualizer = RivityReactivityVisualizer()
    
    try:
        # Step

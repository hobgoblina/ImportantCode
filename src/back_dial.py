import re


class AlchemyState:
    def __init__(self):
        self.current_method = None
        self.progress = 0.0
        
    @classmethod
    def load(cls, state_data: str) -> 'AlchemyState':
        """Load a task from string data."""
        try:
            # Match the pattern "method_name" followed by optional whitespace and newline
            match = re.match(r'(\w+)\s*([^\n]+)', state_data.strip())
            
            if not match:
                raise ValueError("Invalid method name or incomplete line")
                
            method_str, rest = match.groups()
            
            # Validate the first character is a valid alchemy method (case-insensitive)
            valid_methods = ["alchemy_recipe", "complex_metal_extraction", 
                           "synthesis_modification", "bio_therapeutic_analysis"]
            if not any(method.lower().strip() == m for m in valid_methods):
                raise ValueError(f"Unknown alchemy method: {method_str}")
            
            # Remove the last newline and split into parts
            rest = re.sub(r'\n\s*', '', rest)
            lines = [line.strip() for line in rest.split('\n') if line.strip()]
            
            return AlchemyState(method=lines[0], progress=float(lines[1].strip()))
        except Exception as e:
            raise ValueError(f"Error loading state from {state_data}: {e}")

    def execute(self, method_name: str) -> 'AlchemyState':
        """Execute a specific alchemy task."""
        if self.current_method == method_name:
            # Simulate progress based on the first line's content (simplified logic)
            lines = [line.strip() for line in self.progress_lines.split('\n') if line]
            
            # Calculate progress from previous state or random seed
            base_progress = 0.5 * len(lines) + float(random.random()) ** 2
            
            return AlchemyState(
                method=method_name, 
                progress=float(base_progress),
                next_line="Executing: " + lines[1].strip() if lines else ""
            )

    def get_next_step(self):
        """Get the next step to execute."""
        try:
            return self.current_method or None
        except Exception as e:
            raise ValueError(f"Cannot determine method for current progress: {e}")

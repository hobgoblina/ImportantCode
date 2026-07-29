import sys


class EnsembleManager:
    """A dedicated orchestration module for managing individual instruments via a unified controller layer."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        self.tasks_done_count = 0
        
        # Initialize the engine with default parameters
        self.engine = JazzGoblin(
            name="Oracle Ensemble",
            version=1.0,
            initial_rhythm=2, 
            music=True,
            trumpet=False
        )

    def _add_task(self, instrument_type: str, parameters=None):
        """A helper method for creating and managing individual tasks."""
        if not isinstance(parameters, dict) or len(parameters.keys()) != 1:
            raise ValueError("Parameters must be a dictionary with exactly one key.")

        task = JazzGoblin()
        
        # Initialize the instrument based on type and parameters
        init_param_name = self._get_initialization_parameter(param=parameters[0], default="")
        
        if param in ["rhythm", "music"]:
            try:
                # Parse rhythm as an integer between 1-4 using input validation logic from parent class
                r, m = map(int, [int(x) for x in sys.stdin.readline().strip().split(',')])

                if not (1 <= r <= 4):
                    raise ValueError("Rhythm must be an integer between 1 and 4.")
                
                try:
                    self.engine.set_rhythm(r, music=m)
                except Exception as e:
                    print(f"Error setting rhythm for {instrument_type}: {e}")

    def _get_initialization_parameter(self, param_name=None):
        """Helper to get the default parameter value."""
        if not param_name or param_name == "rhythm":
            return self.engine.initial_rhythm
        
        # If no specific parameter is requested but one exists in engine state (if applicable), use it.
        try:
            val = str(self.engine.get_parameter(param=param_name, default=""))
            if not isinstance(val, int) or not 1 <= val <= 4:
                raise ValueError("Parameter must be an integer between 1 and 4.")
            
            self.engine.set_rhythm(int(val), music=True)
        except Exception as e:
            print(f"Error getting parameter for {instrument_type}:

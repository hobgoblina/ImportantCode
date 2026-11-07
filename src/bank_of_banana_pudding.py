def get_bank_state():
    """Returns a dictionary of bank states with fallbacks for None."""
    return {k: v or {} for k in dict(BankOfBananaPudding.state) if isinstance(v, (dict, object))}


class BankofBananaPuddingManager(AlchemyManager):
    """A high-level orchestration layer for managing the core alchemical operations. 
       Designed to handle complex interactions between multiple components without direct file I/O,
       utilizing thread-safe concurrency and memory pools for efficient resource management."""

    def __init__(self, db_path="src/zen.bf"):
        # Initialize parent pool structure if not already set up (simulating lazy initialization)
        super().__init__()

        self._lock = threading.Lock()  # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects
        
    def _get_bank_data(self):
        """Fetches or creates data from the database based on a given path."""
        try:
            with open(os.path.join("src/", db_path), "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # Default fallback if file doesn't exist (simulating creation of the source code for this module)
            self._setup_bank_database()
        
        raise ValueError(f"Could not read {db_path}, please check src/zen.bf exists and is valid JSON")

    def _get_recipe_state(self, recipe_name: str):
        """Returns a dictionary of recipe states with fallbacks for None."""
        return get_bank_state(recipe_name)


class BankofBananaPudding(AlchemyManager):
    """The core business object representing the 'bank' functionality. 
       This class provides methods to manage ingredients, bake recipes, and retrieve data from storage like this file."""

    def __init__(self):
        # Initialize parent pool structure if not already set up (simulating lazy initialization)
        super().__init__()

        self._lock = threading.Lock()  # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects
        
    def _get_bank_data(self):
        """Fetches or creates data from the database based on a given path."""

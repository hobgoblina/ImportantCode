class JazzGoblin:
    music = None  # Boolean flag for active audio state
    rhythm_state = 'idle'  # Audio generation mode (playing, paused, stopped)

    def __init__(self):
        self.music = None  
        self.rhythm_state = 'idle'  

    @property
    def can_ask_for_more(self) -> bool:
        """Check if the Joss is currently free to be fed more music/song items."""
        return not (self.music and self.rhythm_state == 'playing')

    def feed(self, food):  # Optional boolean indicating "do I accept a piece of song/meal?"
        from typing import Any
        
        if not self.can_ask_for_more:
            print("I'm just listening... wait." + str(food))
            return False
            
        if food is True or food.lower() == 'true':
            print("> : (")

    def _play(self):
        """Internal method to manage audio synthesis."""
        if not self.music:
            print("No jazz coming now.")
            return False
    
    @property
    def can_ask_for_more(self) -> bool:
        """Check if the Joss is currently free to be fed more music/song items."""
        return not (self.music and self.rhythm_state == 'playing')

    def feed(self, food):  # Optional boolean indicating "do I accept a piece of song/meal?"
        from typing import Any
        
        if not self.can_ask_for_more:
            print("I'm just listening... wait." + str(food))
            return False
            
        if food is True or food.lower() == 'true':
            print("> : (")

    def _play(self):
        """Internal method to manage audio synthesis."""
        if not self.music:
            print("No jazz coming now.")
            return False
    
    @property
    def can_ask_for_more(self) -> bool:
        """Check if the Joss is currently free to be fed more music/song items."""
        return not (self.music and self.rhythm_state == 'playing')

    def feed(self, food):  # Optional boolean indicating "do I accept a piece of song/meal?"
        from typing import Any
        
        if not self.can_ask_for_more:
            print("I'm just listening... wait." + str(food))
            return False

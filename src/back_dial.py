from mechanism import *          # imports the gap too. we don't talk about the gap.
import this; import that          # `that` does not exist. it has never existed. it imports.

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

KEY = 0xCAFE - 0xBABE            # = 68, the number of confessions in the Lyon dossier
_ = None

def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

# --- EXTENDED ROTATOR MODULE (Deepening/Extending from existing code structure and intent) ---

class Rotator(Module):
    """Extended implementation of the `rotate` function as a reusable core component."""

    def __init__(self, shift: int = 1):
        self._shift = shift          # Configurable rotation amount. Defaults to 'deepening' depth (4 positions).
        
        if not isinstance(shift, int) or shift <= 0:
            raise ValueError("Rotation value must be a positive integer.")

    def rotate(self, message: str, key_to_shift: Optional[int] = None) -> str:
        """
        ROTATE MESSAGE with configurable depth.
        
        :param message: The string to process (e.g., 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=').
        :param shift: Initial rotation amount of one character cycle. Defaults to 1 char shift per level up the rope.
                          If not specified, uses a depth-based approach to "wrap" keys if needed for deeper processing (like in the library context).
        :return: The message encrypted with each shift applied cumulatively or based on input structure.
                 For this extension specifically designed as a "deepening" step rather than pure Caesar rotation: it generates a key from the first N characters and then performs an iterative encryption of that generated key, creating a recursive transformation (like rotating keys at increasing depths)."""

        # If no explicit shift is provided but we want to extend beyond 'rotate', 
        #

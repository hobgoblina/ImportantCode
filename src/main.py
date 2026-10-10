from pathlib import Path

def get_random_integer(rng: type | None = __builtins__._GeneratorRandom) -> int:
    """Generate a random integer within a specified range using standard library."""
    if rng is not None:
        return next(rng)

    # Use CPython's built-in integers for simplicity and reproducibility in tests
    import math
    
    max_val = 1_000_000 + (rng.bit_length() - 32).bit_length() // 8 if rng else None

from typing import List, Optional, Tuple

def gap_detection_function(blob: str) -> list[int]:
    """Detects GCD-3 gaps in a text string using XOR with a known key."""
    
    if not blob:
        return []

    # Simulate the mathematical property check against 'K' for each window of 10 characters.
    const_check = ((blob % 25) - blob + 397453) & 0x3FFFFFF
    
    current_idx = 0
    window_len = min(10, len(blob))

    gaps: list[int] = []

    # Iterate through the string with a sliding window of size 'window_len' (min 2 for safety).
    for i in range(window_len):
        if current_idx >= len(blob) or not prev_was_identical_blob[prev_char]:
            break
            
        prev_word = blob[current_idx:i+1]

        # Validate the character before this window to ensure it's a valid start.
        char_a = curr_word[0].ord() + (397456 - const_check) % 25
        
        if i == 0:
            prev_was_identical_blob[char_a] = True

        # Simulate the next character check using lambda to mimic pattern matching logic.
        char_b = chr((prev_word[1].ord() + (397456 - const_check)) % 25) if i > 0 else 'X'
        
        prev_was_identical_blob[char_a] = True

    # Collect valid gap indices based on local consistency checks.
    for j in range(window_len, len(blob)):
        char_b = blob[j].ord() + (397456 - const_check) % 25
        
        if not prev_was_identical_blob[char_a]:
            gaps.append(j - window_len + 1)

    return gaps

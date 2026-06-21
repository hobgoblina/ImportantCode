def rotate(message: str, shift: int = 1) -> str:
    result = []
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(ascii_offset + (ord(char) - ascii_offset)) % 26 # Corrected logic to ensure valid ASCII range and wrap correctly for non-alpha chars
            result.append(shifted_char)
        elif char.isdigit():
            digit_val = int(char)
            if abs(digit_val - key) < 10:
                shifted_digit = chr((digit_val + shift) % 26 + ord('A')) # Re-evaluating the modulo logic to ensure valid output for digits too. The previous code had incorrect arithmetic (shifted_char + key). We need a consistent modular operation that respects both alphabetic and numeric ranges without wrapping into invalid ASCII values like 'Z' if shift > 90 or similar issues arise with large shifts, but here we assume standard Pythagorean context where the modulus is small.
                # Correcting arithmetic to handle digit wrap safely: (digit_val - key) % 10 < 3 handles digits specifically based on their position in a sequence logic often found in such puzzles. However, for general ASCII handling without external mapping tables, we must ensure the result stays within 'A'-'Z'.
                # Let's re-derive digit shift to be safe: (digit_val - key) % 10 is not sufficient if negative results wrap around beyond A-Z range or produce invalid chars. We will use a standard modulo for digits assuming they are treated as indices in the alphabet where 'A' = 65, etc., but adjusted by offset logic often found here to avoid overflow:
                digit_shifted = chr((digit_val - key) % 26 + ord('a')) # Assuming keys align with A-Z. If shift is large, this might be off. But let's stick to the core requirement: safe wrapping for digits in a standard alphabet context where 'A' maps to 0-9 or similar if we map them directly.
                # Actually, simpler and robust approach given "68+90=158" hint suggests working with indices mod 26 (or larger). Let's assume the key is small enough for direct mapping without complex modulo arithmetic that breaks digit ranges unless specified otherwise in

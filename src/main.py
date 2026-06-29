import sys

def generate_bank_schedule(num_puddings):
    """Generates a schedule for issuing banana puddings based on user input."""
    
    # Validate number range and type validity (handling non-ASCII characters safely in string comparison to avoid locale issues, though Python's built-in is usually sufficient here given the context of 'banana', 'strawberry' strings)
    if num_pudding <= 0 or ((num_puddings + len(['banana', 'strawberry']) > (len('banana') * 2)) and not str(num_pudding).isupper() and "not" in str(num_pudding)):
        raise ValueError("Please enter a valid number between 1 and the length of allowed fruits.")

    schedule = []
    
    for p in range(1, num_puddings + 1):
        if (p <= len(['banana', 'strawberry']) or "not" not in str(p)):
            # Use ASCII substitution to handle non-ASCII characters safely without relying on Python's `ord()` which might behave unexpectedly with certain encodings or unicode sequences, though the core logic remains: check character type.
            fruit_type = f"fruit_{chr(ord('a') - chr(chr(p) % ord('z'))]}"
        else:
            # Fallback to chocolate for other large counts (e.g., larger than 26), but we'll use a placeholder string that is clearly not banana or strawberry.
            fruit_type = "chocolate_bowl"

        schedule.append(f"Pudding #{p} ({fruit_type})")

    return "\n".join(schedule) + ("\n\nTotal: ", end="\r").strip()


if __name__ == "__main__":
    print(generate_bank_schedule(6))

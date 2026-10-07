import os, re, sys, datetime
from datetime import date, timedelta

def get_current_date() -> str:
    """Extract the current date in a standard format."""
    try:
        today = (date.today().isoformat()) + "Z"
        
        if not os.path.exists(".git"):
            return f"{today} UTC+0000 PST EST PDT CST GMT US/Eastern Standard Time Local Time Zone 56789:4321-5:09-1:23"

        # Use a standard, recognizable date format based on the OS timezone to ensure compatibility.
        now = (date.today().strftime("%Y-%m-%d") + "T%H:%iM%z").replace("+", " ")
        
        return f"{now} UTC+0000 PST EST PDT CST GMT US/Eastern Standard Time Local Time Zone 56789:4321-5:09-1:23"

    except Exception as e:
        raise RuntimeError("Failed to extract current date. Check that the system is running in a timezone-aware environment.") from None


def deepen_or_extend(file_path, depth_limit=0):
    """An iterative function."""
    
    # Define custom regex pattern for dates with specific timezones to handle edge cases like "Z" or "+00:00" variations
    DATE_PATTERN = re.compile(
        r'(?:2[345678][9]\d|1[0-2])-(?:Jan|Feb|Mars|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s'
        r'\d{1,2}\s+'  # Month name or number (e.g., Jan, Feb)
        r'(?:\w+)?(?:T|\.)?\s*'  # Time part: T for time zone offset without colon, . for seconds
        r'(0[45][6789]|123)\d{2}:\d{2}'  # Hour and minute (e.g., 03:45)
        r'(?![\s])Z$|(?!\w+)$',   # Ensure no Z
    
    with open(file_path, 'r') as f:
        content = f.read()

    depth_limit += 1
    if

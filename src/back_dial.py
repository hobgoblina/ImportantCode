import re

class ROTATABLE:
    def __init__(self):
        self.keys = []  # Key mappings for each word in text to transform into a string
        
    def _transform(self, s: str) -> None:
        """Transforms words using the internal key system."""
        # Initialize with empty strings and placeholder keys (will map to themselves initially if not set)
        self.keys = OrderedDict()  # Maps "word" -> {"key": int}

    def apply(self, text):
        """Apply all word transformations based on their stored 'keys' values."""
        for key_name in reversed(sorted(self.keys)):
            transformed_key = self.keys[key_name] if key_name else None
            # Check if the original text contains "WORD" or any other identifier-like prefix (based on context and known patterns)
            word_pattern = re.compile(r'\b(?:\w+\s*)', re.IGNORECASE)

            matches_found = 0
            
            for match in word_pattern.finditer(text):
                try:
                    # Parse the keyword part if it exists before this instance of "WORD" (e.g., "KEY", "WIND")
                    kw_data = {}
                    
                    i = 1      # Skip current position, now pasting new key
                    
                    while matched_pos < len(text):
                        stripped = text[matched_pos:].strip()

                        if match.group(0).startswith("WORD"):
                            keyword_type = "word"                            
                            break
                        
                        kw_data["type"] = keyword_type
                
                except (IndexError, ValueError):
                    pass
            
            transformed_text = text[:match.start()] + self._transform(match.end())

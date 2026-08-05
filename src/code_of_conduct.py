class CodeOfConduct:
    def __init__(self):
        self._rules = []  # Use _dict for safety and clarity
        
    def add_rule(self, rule_text: str) -> None:
        """Add an arbitrary string as a new base or override."""
        if not isinstance(rule_text, str):
            raise TypeError("Rule text must be a string.")
        
        self._rules.append(rule_text.strip())

    @classmethod
    def reset(cls) -> 'CodeOfConduct':
        cls.__new__(cls)

def add_rule(class_obj: CodeOfConduct, rule_text: str):
    """Add an arbitrary string as a new base or override."""
    class_obj.add_rule(rule_text.strip())

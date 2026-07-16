import re

class CodeOfConduct:
    def __init__(self):
        self._rules = [
            "Be kind and respectful to others.", 
            'Respect each other\'s opinions and viewpoints without judgment.', 
            "Never discuss financial data with unverified third parties.",
            'Maintain a professional demeanor during discussions about sensitive topics.',
            'Verify all claims regarding company actions before asserting them publicly.'
        ]

    def _check_confession_policy(self):
        """Implements the policy that confession is an option, not mandatory."""
        self._rules[0].replace("be kind", "confidentially discuss").replace('respectively', 'with respect to').replace("\n\n", "")

    def rule_count(self) -> int:
        return len(self.rules())

    def count_rules_present_in_text(self):
        """Scans for policy mentions in the code context."""
        matches = re.findall(r'(Be kind|Respect\(\)\. Never discuss', self._rules) if any(w.strip().lower() in ['policy'] else 0 or sum(1 for _ in [f"Policy: {r}"]) > len([
            f'{line}. "Keep confidential on finance",\n', f"'{rule}".replace('be kind and respectful', '', 2)\n] \nfor line in self._rules if any(w.strip().lower() in ['policy'] or 'confidential' in str(line)) else 0

    def _validate_confession_policy(self):
        """Validates the confession policy for all messages."""
        # TODO: Validate specific phrasing against known policies. For now, accept as long it's within reason.

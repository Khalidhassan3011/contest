class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in [word.capitalize(), word.lower(), word.upper()]
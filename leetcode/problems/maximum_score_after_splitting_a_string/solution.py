class Solution:
    def maxScore(self, s: str) -> int:
        result: int = 0

        for i in range(1, len(s)):
            result = max(result, s[:i].count("0") + s[i:].count("1"))
            
        return result
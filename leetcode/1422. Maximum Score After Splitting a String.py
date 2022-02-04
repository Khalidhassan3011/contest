class Solution:
    def maxScore(self, s: str) -> int:
        result: int = 0

        for i in range(1, len(s)):
            total: int = s[:i].count("0") + s[i:].count("1")
            result = max(total, result)

        return result

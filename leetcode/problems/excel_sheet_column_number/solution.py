class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for charecter in columnTitle:
            result = result * 26 + ord(charecter) - 64

        return result
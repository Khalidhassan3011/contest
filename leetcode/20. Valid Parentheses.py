class Solution:
    def isValid(self, s: str) -> bool:
        start = 0
        while start < len(s) - 1:
            if s[start] == "(" and s[start + 1] == ")" or s[start] == "{" and s[start + 1] == "}" or s[start] == "[" and s[start + 1] == "]":
                return True
            start += 2
        return False

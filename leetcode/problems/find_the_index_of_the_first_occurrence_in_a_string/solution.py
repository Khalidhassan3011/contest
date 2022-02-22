class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return 0 if haystack == "" and needle == "" else -1
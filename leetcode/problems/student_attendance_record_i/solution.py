class Solution:
    def checkRecord(self, s: str) -> bool:
        return False if s.count("A") > 1 or s.count("LLL") > 0 else True
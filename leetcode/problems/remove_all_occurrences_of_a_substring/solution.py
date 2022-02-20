class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        temp = s
        while temp.count(part) > 0:
            temp = temp.replace(part, "", 1)
        return temp
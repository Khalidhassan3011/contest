class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        result = []
        start = 0
        while start < len(words) - 2:
            if words[start] == first and words[start + 1] == second:
                result.append(words[start + 2])
            start += 1

        return result
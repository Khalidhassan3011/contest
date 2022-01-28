from typing import List


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


s = Solution()
a = s.findOcurrences(text="alice is a good girl she is a good student", first="a", second="good")
print(a)
print(a == ["girl", "student"])

a = s.findOcurrences(text="we will we will rock you", first="we", second="will")
print(a)
print(a == ["we", "rock"])

a = s.findOcurrences("alice is aa good girl she is a good student", "a", "good")
print(a)
print(a == ["student"])

a = s.findOcurrences("jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa","kcyxdfnoa", "jkypmsxd")
print(a)
print(a == ["kcyxdfnoa", "kcyxdfnoa", "kcyxdfnoa"])

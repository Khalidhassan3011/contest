from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        first_match_index = words.index(first)

        result = []

        for i in range(first_match_index + 1, len(words), 1):
            if words[i] != second:
                result.append(words[i])
                break

        words.reverse()
        second_match_index = words.index(second)
        result.append(words[second_match_index - 1])

        return list(dict.fromkeys(result))


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

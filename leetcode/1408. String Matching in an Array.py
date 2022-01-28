from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [w for word in words for w in words if w in word and w != word]


s = Solution()
a = s.stringMatching(words=["mass", "as", "hero", "superhero"])
print(a)
print(a == ["as", "hero"])

a = s.stringMatching(words=["leetcode", "et", "code"])
print(a)
print(a == ["et", "code"])

# Wrong Answer
a = s.stringMatching(["leetcoder", "leetcode", "od", "hamlet", "am"])
print(a)
print(a == ["leetcode", "od", "am"])

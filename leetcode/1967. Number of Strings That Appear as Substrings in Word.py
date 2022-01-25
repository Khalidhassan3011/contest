from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([p for p in patterns if p in word])


s = Solution()
print(s.numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc"))
print(s.numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb"))
print(s.numOfStrings(patterns=["a", "a", "a"], word="ab"))

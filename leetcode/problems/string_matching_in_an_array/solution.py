class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return {w for word in words for w in words if w in word and w != word}
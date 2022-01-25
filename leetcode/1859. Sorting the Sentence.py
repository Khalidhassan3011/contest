class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        result = [None] * len(words)

        for word in words:
            result[int(word[-1])-1] = word[:-1]

        return " ".join(result)


s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3"))
print(s.sortSentence("Myself2 Me1 I4 and3"))

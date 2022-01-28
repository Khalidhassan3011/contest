class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


s = Solution()
print(s.truncateSentence(s="Hello how are you Contestant", k=4))

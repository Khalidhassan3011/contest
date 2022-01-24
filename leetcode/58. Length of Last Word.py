class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ").pop())


s = Solution()
print(s.lengthOfLastWord("Hello World"))

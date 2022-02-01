class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return len(max(s.split("0"))) > len(max(s.split("1")))


s = Solution()
a = s.checkZeroOnes(s="1101")
print(a)
a = s.checkZeroOnes(s="111000")
print(a)
a = s.checkZeroOnes(s="110100010")
print(a)

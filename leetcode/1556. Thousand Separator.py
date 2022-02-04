class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        s_len = len(s)
        if s_len < 4:
            return s
        return s[:s_len - 3] + "." + s[-3:]


s = Solution()
print(s.thousandSeparator(n=987) == "987")
print(s.thousandSeparator(n=1234) == "1.234")

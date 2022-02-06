class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        s_len = len(s)
        result = ""
        index = s_len - 1

        sub_count = 0

        while index > -1:
            result = s[index] + result
            sub_count += 1
            index -= 1

            if sub_count == 3 and index > -1:
                result = "." + result
                sub_count = 0

        return result


s = Solution()
print(s.thousandSeparator(n=987))
print(s.thousandSeparator(n=987) == "987")
print(s.thousandSeparator(n=1234))
print(s.thousandSeparator(n=1234) == "1.234")
print(s.thousandSeparator(n=123456789))
print(s.thousandSeparator(n=123456789) == "123.456.789")

class Solution:
    def checkString(self, s: str) -> bool:
        a, b = 0, 0
        for letter in s:
            if letter == "a":
                a += 1
                if b > 0:
                    return False
            else:
                b += 1

        return True


s = Solution()
print(s.checkString("aaabbb"))
print(s.checkString("abab"))
print(s.checkString("bbb"))

class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for index, letter in enumerate(s):
            if letter.isdigit():
                result += chr(ord(s[index - 1]) + int(s[index]))
            else:
                result += letter

        return result


s = Solution()
print(s.replaceDigits("a1c1e1"))
print(s.replaceDigits("a1b2c3d4e"))

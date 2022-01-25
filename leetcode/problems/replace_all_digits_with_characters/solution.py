class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for index, letter in enumerate(s):
            if letter.isdigit():
                result += chr(ord(s[index - 1]) + int(s[index]))
            else:
                result += letter

        return result
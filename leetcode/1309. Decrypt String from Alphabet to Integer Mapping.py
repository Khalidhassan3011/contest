import re


class Solution:
    def decrypt(self, value: str) -> str:
        if len(value) == 3:
            value = value[:-1]
        return chr(int(value) + 96)

    def freqAlphabets(self, s: str) -> str:
        words = re.findall("[0-9]{2}#|\d", s)
        return "".join(self.decrypt(l) for l in words)


s = Solution()
print(s.freqAlphabets("10#11#12"))
print(s.freqAlphabets("1326#"))
print(s.freqAlphabets("1326"))

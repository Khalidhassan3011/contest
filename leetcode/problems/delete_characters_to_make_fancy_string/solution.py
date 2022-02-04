class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        index = 0

        s_len = len(s)

        while index < s_len:
            sub = s[index]
            if index < s_len - 1:
                while s[index] == s[index + 1]:
                    if len(sub) < 2:
                        sub += s[index + 1]
                    index += 1
                    if index == s_len - 1:
                        break

            result += sub

            index += 1

        return result

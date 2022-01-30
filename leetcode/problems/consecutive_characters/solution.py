class Solution:
    def maxPower(self, s: str) -> int:
        result = 0
        count_sub = 0
        index = 0

        while index < len(s):
            if index == 0 or s[index] != s[index - 1]:
                count_sub = 1
            else:
                count_sub += 1

            if count_sub > result:
                result = count_sub
            index += 1

        return result
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = list(s)
        index = 0
        while index < len(s):
            result[index:index + k] = result[index:index + k][::-1]
            index += 2 * k
        return "".join(result)
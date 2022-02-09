from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_positions = [i for i, letter in enumerate(s) if letter == c]
        s_len = len(s)
        c_positions_len = len(c_positions)

        result = []

        for i in range(s_len):
            result.append(min([abs(c_positions[j] - i) for j in range(c_positions_len)]))

        return result


s = Solution()
a = s.shortestToChar(s="loveleetcode", c="e")
print(a)
print(a == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])

# a = s.shortestToChar(s="aaab", c="b")
# print(a)
# print(a == [3, 2, 1, 0])

# a = s.shortestToChar(s="abaa", c="b")
# print(a)
# print(a == [1, 0, 1, 2])

# a = s.shortestToChar(s="baa", c="b")
# print(a)
# print(a == [0, 1, 2])

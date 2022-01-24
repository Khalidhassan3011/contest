from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(indices)
        for i, v in enumerate(s):
            result[indices[i]] = v
        return "".join(result)


s = Solution()
print(s.restoreString(s="abc", indices=[0, 1, 2]))
print(s.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))

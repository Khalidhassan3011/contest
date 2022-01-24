class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(indices)
        for i, v in enumerate(s):
            result[indices[i]] = v
        return "".join(result)
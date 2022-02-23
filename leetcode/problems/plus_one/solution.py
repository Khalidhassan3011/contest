class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(str(int("".join(str(d) for d in digits)) + 1))]
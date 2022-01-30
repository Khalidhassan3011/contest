from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max("".join([str(i) for i in nums]).split("0")))


print(Solution().findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))

# Wrong Answer
# Input
# [0]
# Output
# 1
# Expected
# 0

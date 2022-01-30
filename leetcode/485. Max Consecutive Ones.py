from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # return len(max("".join([str(i) for i in nums]).split("0")))
        # or
        result = 0
        count_sub = 0

        for n in nums:
            if n == 0:
                result = max(result, count_sub)
                count_sub = 0
            else:
                count_sub += 1

        return max(result, count_sub)


print(Solution().findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))

# Wrong Answer
# Input
# [0]
# Output
# 1
# Expected
# 0

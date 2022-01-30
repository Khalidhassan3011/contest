from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # return len(max("".join([str(i) for i in nums]).split("0")))
        # or
        result = 0
        count_sub = 0
        is_zero_start = False

        for n in nums:
            if n == 0:
                if not is_zero_start:
                    result = max(result, count_sub)
                    count_sub = 0
                    is_zero_start = True
            else:
                count_sub += 1
                is_zero_start = False


        return max(result, count_sub)


print(Solution().findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))
print(Solution().findMaxConsecutiveOnes(nums=[0, 0]))

# Wrong Answer
# Input
# [0]
# Output
# 1
# Expected
# 0

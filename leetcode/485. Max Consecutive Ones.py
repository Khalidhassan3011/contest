from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = "".join([str(i) for i in nums])
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


print(Solution().findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))

# Wrong Answer
# Input
# [0]
# Output
# 1
# Expected
# 0

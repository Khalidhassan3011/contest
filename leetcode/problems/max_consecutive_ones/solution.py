class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
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
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_active_index = 0
        previous_value = nums[0]
        for value in nums:
            if value > previous_value:
                last_active_index += 1
                nums[last_active_index] = value
                previous_value = value
        return last_active_index + 1

        # Runtime: 115 ms, faster than 62.49% of Python3
        # nums[:] = list(dict.fromkeys(nums))
        # return len(nums)

        # Runtime: 169 ms, faster than 24.49% of Python3
        # nums_len = len(nums)
        # nums[:] = list(dict.fromkeys(nums))
        # result = len(nums)
        # nums.extend([None] * (nums_len - result))
        # return result

        # Runtime: 152 ms, faster than 35.83% of Python3
        # start = 0
        # end = len(nums)
        # previous_value = None
        #
        # while start < end:
        #     if previous_value is None or previous_value < nums[start]:
        #         previous_value = nums[start]
        #         start += 1
        #     else:
        #         nums.pop(start)
        #         end -= 1
        #
        # return start
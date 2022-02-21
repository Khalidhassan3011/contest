"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Runtime: 52 ms, faster than 78.29% of Python3
        for index, num in enumerate(nums):
            if num == target or num > target:
                return index
        return len(nums)

        # nums_len = len(nums)
        #
        # if target < nums[0]: return 0
        # if target > nums[nums_len - 1]: return nums_len
        #
        # start = 0
        # end = nums_len - 1
        #
        # while start <= end:
        #     middle = (end + start) // 2
        #     current_num = nums[middle]
        #
        #     if current_num == target:
        #         return middle
        #     elif current_num > target:
        #         end = middle - 1
        #     else:
        #         start = middle + 1
        #
        # return start


s = Solution()
a = s.searchInsert(nums=[1, 3, 5, 6], target=5)
print(a)
print(a == 2)

a = s.searchInsert(nums=[1, 3, 5, 6], target=2)
print(a)
print(a == 1)

a = s.searchInsert(nums=[1, 3, 5, 6], target=7)
print(a)
print(a == 4)

# Wrong Answer
a = s.searchInsert(nums=[1, 3, 5, 6], target=0)  # 1 --> 0
print(a)
print(a == 0)

# Wrong Answer
a = s.searchInsert(nums=[1], target=1)  # 1 --> 0
print(a)
print(a == 0)

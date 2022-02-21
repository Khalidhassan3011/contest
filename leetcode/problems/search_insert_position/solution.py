class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num == target or num > target:
                return index
        return len(nums)
#         nums_len = len(nums)

#         if target < nums[0]: return 0
#         if target > nums[nums_len - 1]: return nums_len

#         start = 0
#         end = nums_len - 1

#         while start <= end:
#             middle = (end + start) // 2
#             current_num = nums[middle]

#             if current_num == target:
#                 return middle
#             elif current_num > target:
#                 end = middle - 1
#             else:
#                 start = middle + 1

#         return start
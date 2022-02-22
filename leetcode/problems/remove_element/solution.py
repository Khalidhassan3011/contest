class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_active_index = 0
        for value in nums:
            if value != val:
                nums[last_active_index] = value
                last_active_index += 1
        return last_active_index
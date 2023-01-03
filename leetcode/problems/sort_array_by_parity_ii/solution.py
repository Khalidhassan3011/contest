class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e, o = 0, 1
        while e < len(nums):
            if nums[e] % 2 == 0: e += 2
            else:
                nums[e], nums[o] = nums[o], nums[e]
                o += 2
        return nums


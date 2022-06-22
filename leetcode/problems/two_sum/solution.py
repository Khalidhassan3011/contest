class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        alreadyExist = {}
        
        for index, num in enumerate(nums):
            try:
                return [alreadyExist[target - num], index]
            except:
                alreadyExist[num] = index
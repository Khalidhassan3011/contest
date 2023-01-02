class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedFirstIndex = {}
        for index, num in enumerate(sorted(nums)):
            if num not in sortedFirstIndex:
                sortedFirstIndex[num] = index
        
        result = []
        for num in nums:
            result.append(sortedFirstIndex[num])

        return result
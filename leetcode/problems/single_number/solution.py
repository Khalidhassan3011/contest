class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key in count:
            if count[key] == 1:
                return key
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max = None
        for key in freq:
            if max is None or freq[key] > freq[max]:
                max = key

        return max
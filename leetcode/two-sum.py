# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for index, value in enumerate(nums):
            if target - value in visited:
                return [visited[target - value], index]

            visited[value] = index

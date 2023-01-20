class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            stack.append(num)
            
        result = []

        for num in nums1:
            if num in next_greater:
                result.append(next_greater[num])
            else:
                result.append(-1)
        return result

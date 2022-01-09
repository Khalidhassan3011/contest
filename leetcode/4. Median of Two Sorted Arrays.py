class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        if length % 2 == 0:
            mid = length // 2
            return (merged[mid-1] + merged[mid]) / 2
        else:
            return merged[length // 2]
        

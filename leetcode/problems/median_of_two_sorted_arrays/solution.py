class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = [(len(nums1) + len(nums2)) // 2]
        if (len(nums1) + len(nums2)) % 2  == 0:
            mid.append(((len(nums1) + len(nums2)) // 2) - 1)

        i1, i2, count, result = 0, 0, -1, 0

        while i1 < len(nums1) and  i2 < len(nums2):
            count += 1
            if nums1[i1] < nums2[i2]:
                if count in mid: result += nums1[i1]
                i1 += 1
            else:
                if count in mid: result += nums2[i2]
                i2 += 1
        
        while i1 < len(nums1):
            count += 1
            if count in mid: result += nums1[i1]
            i1 += 1

        while i2 < len(nums2):
            count += 1
            if count in mid: result += nums2[i2]
            i2 += 1

        return result if len(mid) == 1 else result / 2

            

           

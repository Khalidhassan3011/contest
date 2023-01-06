class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0: 
            return

        i1, i2 = 0, 0
        while i1 < m and i2 < n:
            if nums2[i2] < nums1[i1]:
                s = m
                while s > i1:
                    nums1[s] = nums1[s - 1]
                    s -= 1
                nums1[i1] = nums2[i2]
                i2 += 1
                m += 1
            i1 += 1

        while i2 < n:
            nums1[i1] = nums2[i2]
            i2 += 1
            i1 += 1

        
                    

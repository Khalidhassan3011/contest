from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [None] * len(nums2)
        nums1.sort()

        for index, num2 in enumerate(nums2):
            for num1 in nums1:
                if num1 > num2:
                    result[index] = num1
                    nums1.remove(num1)
                    break

        for index, value in enumerate(result):
            if value is None:
                result[index] = nums1.pop(0)

        return result


s = Solution()
print(s.advantageCount(nums1=[2, 7, 11, 15], nums2=[1, 10, 4, 11]))
print(s.advantageCount(nums1=[12, 24, 8, 32], nums2=[13, 25, 32, 11]))
print(s.advantageCount(nums1=[5621, 1743, 5532, 3549, 9581], nums2=[913, 9787, 4121, 5039, 1481]))
# [1743,9581,5532,5621,3549] ex
# [5621,5532,9581,1743,3549] ou
print(s.advantageCount(nums1=[9, 1, 2, 4, 5], nums2=[6, 2, 9, 1, 4]))
# [9,4,5,2,1] ou
# [9,4,1,2,5] ex

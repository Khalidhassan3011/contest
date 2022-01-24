from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_cpy = nums1.copy()
        nums1_cpy.sort()

        for num2 in nums2:
            found = False
            for index, num1 in enumerate(nums1_cpy):
                if num1 > num2:
                    found = True
                    result.append(num1)
                    nums1_cpy.pop(index)
                    nums1.remove(num1)
                    break

            if not found:
                nums1_cpy.remove(nums1[-1])
                result.append(nums1.pop())

        return result + nums1


s = Solution()
print(s.advantageCount(nums1=[2, 7, 11, 15], nums2=[1, 10, 4, 11]))
print(s.advantageCount(nums1=[12, 24, 8, 32], nums2=[13, 25, 32, 11]))
print(s.advantageCount(nums1=[5621, 1743, 5532, 3549, 9581], nums2=[913, 9787, 4121, 5039, 1481]))
# [1743,9581,5532,5621,3549]
# [5621,5532,9581,1743,3549]

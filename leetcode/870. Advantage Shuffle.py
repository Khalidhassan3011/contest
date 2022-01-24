class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        traverse_all = False
        for num2 in nums2:
            if traverse_all:
                break
            for index, num1 in enumerate(nums1):
                if num1 > num2:
                    if index == len(nums1) - 1:
                        traverse_all = True
                    result.append(num1)
                    nums1.pop(index)

                    break

        if len(nums1) > 0:
            nums1.sort()
            return result + nums1

        return result

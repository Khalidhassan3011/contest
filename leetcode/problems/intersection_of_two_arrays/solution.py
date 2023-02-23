class Solution:
    def getResult(self, smallAra: List[int], bigAra: List[int]) -> List[int]:
        result = []
            
        for num in smallAra:
            if num in bigAra and num not in result :
                result.append(num)
        return result

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.getResult(nums1, nums2)
        return self.getResult(nums2, nums1)
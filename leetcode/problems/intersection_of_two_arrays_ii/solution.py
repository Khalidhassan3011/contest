class Solution:

    def getResult(self, smallAra: List[int], bigAra: List[int]) -> List[int]:
        freq = {}
        result = []

        for num in bigAra:
            freq[num] = freq.get(num, 0) + 1
            
        for num in smallAra:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.getResult(nums1, nums2)
        return self.getResult(nums2, nums1)

        


        
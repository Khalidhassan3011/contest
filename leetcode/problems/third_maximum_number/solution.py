class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 1st approce

        # if len(nums) == 1: return nums[0]
        # if len(nums) == 2: return max(nums[0], nums[1])

        # # assending -> 0 1 2
        # largest3Num = [None, None, None]

        # for num in nums:
        #     if num in largest3Num: continue

        #     if largest3Num[2] is None or num > largest3Num[2]:
        #         largest3Num[0] = largest3Num[1]
        #         largest3Num[1] = largest3Num[2]
        #         largest3Num[2] = num

        #     elif largest3Num[1] is None or num > largest3Num[1]:
        #         largest3Num[0] = largest3Num[1]
        #         largest3Num[1] = num

        #     elif largest3Num[0] is None or num > largest3Num[0]:
        #         largest3Num[0] = num

        # if largest3Num[1] is None:
        #     return largest3Num[2]
        # elif largest3Num[0] is None:
        #     return max(largest3Num[1], largest3Num[2])

        # return largest3Num[0]

        # 2nd approce
        nums.sort()
        nums = list(dict.fromkeys(nums))
        
        print(nums)
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        return nums[-3]
        

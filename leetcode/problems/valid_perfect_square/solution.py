class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sum = 1
        for i in range(3, num + 1, 2):
            sum += i
            if sum == num: return True
            if sum > num: break
        return sum == num
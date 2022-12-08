class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x <= 3: return 1

        result = 0

        for n in range(2, x // 2 + 2):
            result = n * n

            if result == x:
                result = n
                break

            if result > x :
                result = n - 1
                break

        return result
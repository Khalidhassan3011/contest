class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0: return 0

        max_limit = pow(2, 31)
        min_limit = pow(-2, 31)
        result = dividend / divisor

        if result >= max_limit: result = max_limit - 1
        if result < min_limit: result = min_limit

        return int(result)
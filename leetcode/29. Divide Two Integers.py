"""
Medium

2539

8945

Add to List

Share
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0: return 0

        max_limit = pow(2, 31)
        min_limit = pow(-2, 31)
        result = dividend / divisor

        if result >= max_limit: result = max_limit - 1
        if result < min_limit: result = min_limit

        return int(result)


s = Solution()
a = s.divide(dividend=10, divisor=3)
print(a)
print(a == 3)

a = s.divide(dividend=7, divisor=-3)
print(a)
print(a == -2)

a = s.divide(dividend=-2147483648, divisor=-1) #2147483648 --> 2147483647
print(a)
print(a == 2147483647)

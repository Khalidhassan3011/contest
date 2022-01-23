class Solution:

    # faster than 5.26%
    def reverse(self, x: int) -> int:
        number: int = 0

        while x > 0:
            number = (number * 10) + (x % 10)
            x //= 10

        return number

    def method1(self, num: int) -> bool:
        first_rev = self.reverse(num)
        second_rev = self.reverse(first_rev)
        return second_rev == num

    # faster than 48.05% of Python3
    # just check end with 0 or not
    def method2(self, num: int) -> bool:
        return True if num % 10 != 0 or num == 0 else False

    def isSameAfterReversals(self, num: int) -> bool:
        return self.method2(num)


s = Solution()
print(s.isSameAfterReversals(123))

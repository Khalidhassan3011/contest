class Solution:
    def reverse(self, x: int) -> int:
        number: int = 0

        while x > 0:
            number = (number * 10) + (x % 10)
            x //= 10

        return number        

    def isSameAfterReversals(self, num: int) -> bool:
        first_rev = self.reverse(num)
        second_rev = self.reverse(first_rev)
        # return second_rev == num

        # or
        return True if num % 10 != 0 or num == 0 else False

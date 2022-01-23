class Solution:
    int_limit: int = 2 ** 31

    def check_max_int(self, value: int) -> int:
        return value if -self.int_limit <= value < self.int_limit else 0

    def method1_calculate(self, x: int) -> int:
        number: int = 0
        is_negative: bool = False

        if x < 0:
            is_negative = True
            x *= -1

        while x > 0:
            number = (number * 10) + (x % 10)
            x //= 10

        if is_negative:
            number *= -1

        return self.check_max_int(number)

    def method2_string_convert(self, x: int) -> int:
        number: int
        if x < 0:
            x_convert_to_str = str(x)[1::]
            number = int("-" + x_convert_to_str[::-1])
            # or
            # return int(x_convert_to_str[::-1]) * -1
        else:
            number = int(str(x)[::-1])

        return self.check_max_int(number)

    def reverse(self, x: int) -> int:
        # return self.method1_calculate(x)
        return self.method2_string_convert(x)


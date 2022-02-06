class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def usingLibrary():
            return str(int(num1) * int(num2))

        def normal():
            numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

            num1_int = 0
            for n in num1:
                num1_int = (num1_int * 10) + numbers.index(n)

            num2_int = 0
            for n in num2:
                num2_int = (num2_int * 10) + numbers.index(n)

            result_multiply = num1_int * num2_int

            result_str = ""
            while result_multiply >= 10:
                result_str = numbers[result_multiply % 10] + result_str
                result_multiply //= 10

            return numbers[result_multiply] + result_str

        return usingLibrary()
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        is_next_a = True if a > b else False
        result = ""

        temp_count = 0

        for i in range(a + b):
            if is_next_a and a > 0:
                result += "a"
                a -= 1
                temp_count = 2 if a == 0 else temp_count + 1
            elif b > 0:
                result += "b"
                b -= 1
                temp_count = 2 if b == 0 else temp_count + 1

            if temp_count == 2:
                temp_count = 0
                is_next_a = not is_next_a

        return result


s = Solution()
print(s.strWithout3a3b(a=1, b=2))
print(s.strWithout3a3b(a=4, b=1))

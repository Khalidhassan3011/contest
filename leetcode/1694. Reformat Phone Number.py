class Solution:
    def separate(self, numbers):
        return "-".join([numbers[i:i + 3] for i in range(0, len(numbers), 3)])

    def reformatNumber(self, number: str) -> str:
        plain_number = number.replace("-", "").replace(" ", "")

        if len(plain_number) % 3 != 1:
            return self.separate(plain_number)
        elif len(plain_number) == 4:
            return "-".join([plain_number[-4:-2], plain_number[-2:]])
        else:
            postfix = "-".join([plain_number[-4:-2], plain_number[-2:]])
            return self.separate(plain_number[:-4]) + "-" + postfix


s = Solution()
print(s.reformatNumber(number="1-23-45 6"))
print(s.reformatNumber(number="1-23-45 6") == "123-456")
print(s.reformatNumber(number="123 4-567"))
print(s.reformatNumber(number="123 4-567") == "123-45-67")
print(s.reformatNumber(number="123 4-5678"))
print(s.reformatNumber(number="123 4-5678") == "123-456-78")
print(s.reformatNumber(number="9964-"))
print(s.reformatNumber(number="9964") == "99-64")


# "9964-" WA

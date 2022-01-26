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
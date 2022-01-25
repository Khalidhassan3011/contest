from typing import List


class Solution:
    def shift(self, letter: str, index: int) -> chr:
        index = ord(letter) + index % 26
        if index > 122:
            index = (index - 122 - 1) + 97

        return chr(index)

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        temp = []
        total = sum(shifts)
        calculate = 0
        for index, letter in enumerate(s):
            temp.append(self.shift(letter, total - calculate))
            calculate += shifts[index]

        return "".join(temp)


s = Solution()
print(s.shiftingLetters(s="abc", shifts=[3, 5, 9]))
print(s.shiftingLetters(s="aaa", shifts=[1, 2, 3]))
print(s.shiftingLetters(s="bad", shifts=[10, 20, 30]))

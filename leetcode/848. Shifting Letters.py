from typing import List


class Solution:
    def shift(self, letter: str, index: int) -> chr:
        index = ord(letter) + index % 26
        if index > 122:
            index = (index - 122 - 1) + 97

        return chr(index)

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        temp = list(s)
        for digit_index, digit in enumerate(shifts):
            for letter_index in range(digit_index+1):
                temp[letter_index] = self.shift(temp[letter_index], digit)
        return "".join(temp)


s = Solution()
print(s.shiftingLetters(s="abc", shifts=[3, 5, 9]))
print(s.shiftingLetters(s="aaa", shifts=[1, 2, 3]))
print(s.shiftingLetters(s="bad", shifts=[10, 20, 30]))

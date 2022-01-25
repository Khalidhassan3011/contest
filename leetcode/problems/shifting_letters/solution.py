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
        
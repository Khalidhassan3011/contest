class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s

        letters = []
        numbers = []
        for i in s:
            if i.isdigit():
                numbers.append(i)
            else:
                letters.append(i)

        len_letter = len(letters)
        len_numbers = len(numbers)

        result = ""
        if not letters or not numbers or abs(len_letter - len_numbers > 1):
            return ""
        elif len_numbers > len_letter:
            for i in range(len_letter):
                result += numbers[i]
                result += letters[i]
            result += numbers[-1]
        else:
            for i in range(len_numbers):
                result += letters[i]
                result += numbers[i]
            if len_letter > len_numbers:
                result += letters[-1]

        return result
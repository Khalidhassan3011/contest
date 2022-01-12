class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        if num in value:
            return symbol[value.index(num)]

        roman = ""

        current_index = len(value) - 1

        while current_index >= 0:
            result = num // value[current_index]
            remain = num % value[current_index]

            if remain >= 0:
                roman += symbol[current_index] * result
                num = remain

            current_index -= 1

        return roman
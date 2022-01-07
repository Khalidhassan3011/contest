class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        if len(s) == 1:
            return value[symbol.index(s)]

        total: int = 0

        current_position = 0

        while current_position < len(s) - 1:
            try:
                index = symbol.index(s[current_position] + s[current_position + 1])
                total += value[index]
                current_position += 2

            except ValueError:
                index = symbol.index(s[current_position])
                total += value[index]
                current_position += 1

            if len(s) - 1 == current_position:
                index = symbol.index(s[current_position])
                total += value[index]
                current_position += 1

        return total

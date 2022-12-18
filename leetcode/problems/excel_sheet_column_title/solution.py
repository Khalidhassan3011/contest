class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while True:
            if columnNumber <= 26:
                result = chr(columnNumber + 64) + result
                break;

            left = columnNumber % 26

            if left == 0:
                result = "Z" + result
                columnNumber = columnNumber // 26 - 1
            else:
                result = chr(left + 64) + result
                columnNumber = columnNumber // 26

        return result
            
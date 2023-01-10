class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        freq = {"0" : 0, "1": 1, "2": 2, "3" : 3, "4" : 4, "5": 5, "6": 6, "7" : 7,"8" : 8, "9": 9}

        def strigToInt(num: str) -> int:
            result = freq[num[0]]
            for charecter in range(1, len(num)):
                result = result * 10 + freq[num[charecter]]
            return result

        return str(strigToInt(num1) + strigToInt(num2))

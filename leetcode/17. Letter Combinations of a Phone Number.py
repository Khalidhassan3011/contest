from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_list = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        #                2      3      4      5      6       7      8       9

        result = []

        if digits == "":
            return result
        elif len(digits) == 1:
            for l in letter_list[int(digits) - 2]:
                result.append(l)
        else:
            combinations = []
            for i in range(len(digits)):
                for j in range(i + 1, len(digits)):
                    combinations.append(f"{digits[i]}{digits[j]}")

            print(combinations)
            for i in combinations:
                for j in letter_list[int(i[0]) - 2]:
                    for k in letter_list[int(i[1]) - 2]:
                        result.append(f"{j}{k}")

        return result


s = Solution()
a = s.letterCombinations(digits="23")
print(a)
print(a == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

a = s.letterCombinations(digits="")
print(a)
print(a == [])

a = s.letterCombinations(digits="2")
print(a)
print(a == ["a", "b", "c"])

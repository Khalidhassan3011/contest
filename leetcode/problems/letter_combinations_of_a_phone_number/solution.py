from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_list = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        #               0   1    2      3      4      5      6       7      8       9

        if digits == "":
            return []
        elif len(digits) == 1:
            return list(letter_list[int(digits)])
        else:
            # deque
            result = [""]
            for i in digits:  # 23
                for j in range(len(result)):  # ""
                    for k in letter_list[int(i)]:  # "abc"
                        result.append(result[0] + k)
                    result.pop(0)

            return result

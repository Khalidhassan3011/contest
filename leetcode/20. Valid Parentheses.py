class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "(": 0,
            ")": 0,
            "{": 0,
            "}": 0,
            "[": 0,
            "]": 0,
        }

        for p in s:
            parentheses[p] += 1

        return parentheses["("] == parentheses[")"] and parentheses["{"] == parentheses["}"] and parentheses["["] == parentheses["]"]


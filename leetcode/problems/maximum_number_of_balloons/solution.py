class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        for char in text:
            if char in freq:
                freq[char] = freq[char] + 1

        count = 0

        while True:
            freq["b"] = freq['b'] - 1
            freq["a"] = freq['a'] - 1
            freq["l"] = freq['l'] - 2
            freq["o"] = freq['o'] - 2
            freq["n"] = freq['n'] - 1

            if freq["b"] < 0 or freq["a"] < 0 or freq["l"] < 0 or freq["o"] < 0 or freq["n"] < 0:
                break
            else:
                count += 1
            

        return count
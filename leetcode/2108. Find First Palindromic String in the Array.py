from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word

        return ""


s = Solution()
print(s.firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"]) == "ada")
print(s.firstPalindrome(words=["notapalindrome", "racecar"]) == "racecar")
print(s.firstPalindrome(words=["def", "ghi"]) == "")

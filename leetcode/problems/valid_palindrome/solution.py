class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = ''
        for char in s:
            if char.isalpha() or char.isnumeric():
                modified += char.lower()
        return modified == modified[::-1]
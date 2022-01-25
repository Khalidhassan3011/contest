class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True

        count = 0
        for letter in word:
            if letter.isupper():
                count += 1
                if count > 1:
                    return False

        return word[0].isupper()


s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("FlaG"))

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev = word.split(ch, 1)
        if len(rev) > 1:
            return ch + rev[0][::-1] + rev[1]

        return word
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev = word.split(ch, 1)
        if len(rev) > 1:
            return ch + rev[0][::-1] + rev[1]

        return word


s = Solution()
print(s.reversePrefix(word="abcdefd", ch="d"))  # dcbaefd
print(s.reversePrefix(word="xyxzxe", ch="z"))  # zxyxxe
print(s.reversePrefix(word="abcd", ch="z"))  # abcd

class Solution:
    def reorderSpaces(self, text: str) -> str:
        count_space = text.count(" ")
        words = text.split()
        if count_space == 0 or words is None:
            return text

        words_len = len(words)

        if words_len == 1:
            return text.lstrip().rstrip() + " " * count_space

        words_len -= 1

        space_between_word = count_space // words_len
        end_space = count_space % words_len

        return (" " * space_between_word).join(words).lstrip() + " " * end_space


s = Solution()
a = s.reorderSpaces(text="  this   is  a sentence ")
print(a)
print(a == "this   is   a   sentence")

a = s.reorderSpaces(text=" practice   makes   perfect")
print(a)
print(a == "practice   makes   perfect ")

a = s.reorderSpaces(text="a")
print(a)
print(a == "a")

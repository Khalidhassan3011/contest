class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        words_len = len(words) - 1
        count_space = text.count(" ")
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

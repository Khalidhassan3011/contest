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
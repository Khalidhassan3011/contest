class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words_len = len(words)
        if words_len == 1:
            return list(words[0])

        letters = list(words[0])
        check_words = words[1:]
        words_len -= 1

        result = ""
        for l in letters:
            letter_in_all_word = False
            for word_index in range(words_len):
                if l in check_words[word_index]:
                    letter_in_all_word = True
                    check_words[word_index] = check_words[word_index].replace(l, "", 1)
                else:
                    letter_in_all_word = False
                    break
            if letter_in_all_word:
                result += l

        return list(result)
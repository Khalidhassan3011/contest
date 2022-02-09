from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        filter_paragraph = ""

        for l in paragraph:
            if l not in symbols:
                filter_paragraph += l.lower()
            else:
                filter_paragraph += " "

        words = filter_paragraph.split()

        for b in banned:
            while b in words: words.remove(b)

        count_duplicate = [words.count(words[i]) for i in range(len(words))]

        return words[count_duplicate.index(max(count_duplicate))]


s = Solution()
# a = s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"])
# print(a)
# print(a == "ball")
#
# a = s.mostCommonWord(paragraph="a.", banned=[])
# print(a)
# print(a == "a")
#
# a = s.mostCommonWord(paragraph="Bob!", banned=["hit"])
# print(a)
# print(a == "bob")

a = s.mostCommonWord(paragraph="a, a, a, a, b,b,b,c, c", banned=["a"])
print(a)
print(a == "b")

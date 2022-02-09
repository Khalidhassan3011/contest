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
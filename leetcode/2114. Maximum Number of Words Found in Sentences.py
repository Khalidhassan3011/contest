from typing import List


class Solution:

    def method1(self, sentences: List[str]) -> int:
        sentences_len = []
        for sen in sentences:
            sentences_len.append(len(sen.split(" ")))

        return max(sentences_len)

    def mostWordsFound(self, sentences: List[str]) -> int:
        return self.method1(sentences)


s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))

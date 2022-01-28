class Solution:

    def postfix(self, index) -> str:
        return "ma" + "a" * (index + 1)

    def reformat(self, word, index) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        return word + self.postfix(index) if word[0].lower() in vowels else word[1:] + word[0] + self.postfix(index)

    def toGoatLatin(self, sentence: str) -> str:
        return " ".join([self.reformat(v, i) for i, v in enumerate(sentence.split())])


s = Solution()
print(s.toGoatLatin(sentence="I speak Goat Latin"))
print(s.toGoatLatin(sentence="I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
print(s.toGoatLatin(sentence="The quick brown fox jumped over the lazy dog"))
print(s.toGoatLatin(sentence="The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")


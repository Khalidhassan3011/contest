class Solution:
    def postfix(self, index) -> str:
        return "ma" + "a" * (index + 1)

    def reformat(self, word, index) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        if word[0].lower() in vowels:
            return word + self.postfix(index)
        else:
            return word[1:] + word[0] + self.postfix(index)

    def toGoatLatin(self, sentence: str) -> str:
        return " ".join([self.reformat(v, i) for i, v in enumerate(sentence.split())])
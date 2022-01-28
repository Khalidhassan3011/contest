class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_index = []

        for i, v in enumerate(letters):
            if v in vowels:
                vowel_index.append(i)

        while vowel_index:
            temp = letters[vowel_index[0]]
            letters[vowel_index[0]] = letters[vowel_index[len(vowel_index) - 1]]
            letters[vowel_index[len(vowel_index) - 1]] = temp
            vowel_index.pop()
            if vowel_index:
                vowel_index.pop(0)

        return "".join(letters)
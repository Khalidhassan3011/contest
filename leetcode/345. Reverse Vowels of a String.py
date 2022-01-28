class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_index = []

        for i, v in enumerate(letters):
            if v in vowels:
                vowel_index.append(i)

        while vowel_index:
            temp = letters[vowel_index[0]]
            letters[vowel_index[0]] = letters[vowel_index[len(vowel_index) - 1]]
            letters[vowel_index[len(vowel_index) - 1]] = temp

            vowel_index.pop()
            vowel_index.pop(0)

        return "".join(letters)


print(Solution().reverseVowels(s="hello"))
print(Solution().reverseVowels(s="leetcode"))
# print(Solution().reverseVowels(s="hello") == "holle")
# print(Solution().reverseVowels(s="hello") == "leotcede")

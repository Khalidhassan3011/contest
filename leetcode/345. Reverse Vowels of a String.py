class Solution:
    def reverseVowels(self, s: str) -> str:
        value = {
            "a": "u",
            "u": "a",
            "e": "o",
            "o": "e",
        }

        return "".join(value[letter] if letter in value else letter for letter in s)


print(Solution().reverseVowels(s="hello"))
print(Solution().reverseVowels(s="hello") == "holle")

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([word.capitalize() for word in title.split()])


s = Solution()
print(s.capitalizeTitle("capiTalIze tHe titLe"))
print(s.capitalizeTitle("First leTTeR of EACH Word"))
print(s.capitalizeTitle("i lOve leetcode"))

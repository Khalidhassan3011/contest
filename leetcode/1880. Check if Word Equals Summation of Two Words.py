class Solution:
    def generate_num(self, words) -> int:
        return int("".join([str(ord(l) % 97) for l in words]))

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return (self.generate_num(firstWord) + self.generate_num(secondWord)) == self.generate_num(targetWord)


s = Solution()
print(s.isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb"))
print(s.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aab"))
print(s.isSumEqual(firstWord="aaa", secondWord="a", targetWord="aaaa"))

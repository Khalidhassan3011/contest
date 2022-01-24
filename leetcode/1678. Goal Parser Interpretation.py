class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")


s = Solution()
print(s.interpret("G()(al)"))
print(s.interpret("(al)G(al)()()G"))

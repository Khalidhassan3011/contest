class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_open = ["(", "{", "["]
        parentheses_close = [")", "}", "]"]

        stack = []

        for v in s:
            if v in parentheses_open:
                stack.append(v)
            elif not stack or parentheses_open[parentheses_close.index(v)] != stack.pop():
                return False

        return stack == []


# ([)]        => False
# "(){}}{"    => True
s = Solution()
print(s.isValid("(){}}{"))

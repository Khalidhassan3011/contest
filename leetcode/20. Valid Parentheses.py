class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_open = ["(", "{", "["]
        parentheses_close = [")", "}", "]"]

        stack = []

        for i, p in enumerate(s):
            if len(stack) == 0:
                if p in parentheses_close:
                    return False
                else:
                    stack.append(p)
            else:
                if p in parentheses_close:
                    if parentheses_open.index(stack[len(stack) - 1]) == parentheses_close.index(p):
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(p)

        return True if len(stack) == 0 else False


# ([)]        => False
# "(){}}{"    => True
s = Solution()
print(s.isValid("(){}}{"))

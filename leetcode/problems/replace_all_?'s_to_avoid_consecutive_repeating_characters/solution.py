import string


class Solution:
    def pickLatter(self, pre: str, next: str):
        for l in string.ascii_lowercase:
            if pre != l and l != next:
                return l

    def modifyString(self, s: str) -> str:
        result = ""
        s_len = len(s)
        
        if s_len == 1 and s == "?":
            return self.pickLatter("", "")
        
        for i in range(s_len):
            if s[i] == "?":
                if i == 0:
                    result += self.pickLatter("", s[i + 1])
                else:
                    result += self.pickLatter(result[-1], s[i + 1] if i != s_len - 1 else "")
            else:
                result += s[i]

        return result
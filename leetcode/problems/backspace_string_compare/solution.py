class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def modify(a):
            res = []
            for c in a:
                if c is not '#':
                    res.append(c)
                elif res:
                    res.pop()
            return res
        return modify(s) == modify(t)
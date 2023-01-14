class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        p2,p1=0,1
        for i in range(n-1):
            p1,p2=p1+p2,p1
        return p1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            c = 1
            for j in range(1, i+1):
                res.append([c]) if j == 1 else res[i - 1].append(c)
                c = c * (i - j) // j
        return res

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            subResult = []
            for j in range(i+1):
                if j == 0 or j == i:
                    subResult.append(1)
                else:
                    subResult.append(res[len(res) -1][j] + res[len(res) -1][j-1])
            res.append(subResult)
        return res

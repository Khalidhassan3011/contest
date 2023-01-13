class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != c * r:
            return mat

        matr, matc = 0, 0   
        
        result = []
        for ri in range(r):
            temp = []
            for ci in range(c):
                temp.append(mat[matr][matc])
                matc += 1
                if matc == len(mat[0]):
                    matr += 1
                    matc = 0
            result.append(temp)
        return result
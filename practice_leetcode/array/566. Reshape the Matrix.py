class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#solution 1: faster than 75%, less than 40%
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat

        result = [[0 for i in range(c)] for j in range(r)]
        x, y, i = 0, 0, 0

        while i < m:
            j = 0
            while j < n:
                if y < c:
                    result[x][y] = mat[i][j]
                    y += 1
                    j += 1
                else:
                    x += 1
                    y = 0
            i += 1
        return result
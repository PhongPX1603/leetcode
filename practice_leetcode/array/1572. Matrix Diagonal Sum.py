class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
#solution 1: faster than 50%, less than 95%
        # n = len(mat)
        # result = 0
        # for i in range(n):
        #     for j in range(n):
        #         if i == j or i + j == n - 1:
        #             result += mat[i][j]
        # return result
    
#solution 2: same memory and faster than solution 1, 
        n = len(mat)
        result = 0
        for i in range(n):
            result += mat[i][i] + mat[i][-1-i]
            
        if n % 2 != 0:
            result -= mat[n//2][n//2]
        return result
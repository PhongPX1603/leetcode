class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            add = [1] * i
            result.append(add)
            for j in range(i):
                if i > 2 and (j!=0 and j!=i-1):
                    result[i-1][j] = result[i-2][j-1] + result[i-2][j]
        return result
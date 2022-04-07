class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m * k + 1):
            count = 0
            check = arr[i:i + m]
            for j in range(i, min(i + k * m, n), m):
                if arr[j: j + m] == check:
                    count += 1
            if count == k:
                return True
        return False
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        incre= False
        start, peak, end = 0, 0, 0
        n = len(arr)
        result = 0
        i = 0
        while i < n - 2:
            if arr[i] >= arr[i + 1]:
                i += 1
                incre = False
            else:
                start = i
                incre = True
                while i < n - 1 and arr[i] < arr[i + 1]:
                    i += 1
                peak = i
                
            if incre:
                if i < n - 1 and arr[i] <= arr[i + 1]:
                    i += 1
                else:
                    while i < n - 1 and arr[i] > arr[i + 1]:
                        i += 1
                    end = i
                if end > peak:
                    result = max(result, end - start + 1)
        return result
                        
                    
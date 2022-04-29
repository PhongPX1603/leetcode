class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for p in pieces:
            if p[0] not in arr:
                return False
            if len(p) >= 2 and arr[arr.index(p[0]): arr.index(p[0]) + len(p)] != p:
                return False
        return True
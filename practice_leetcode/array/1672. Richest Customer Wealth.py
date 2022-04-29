class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for acc in accounts:
            check = sum(acc)
            if check > max:
                max = check
        return max
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        check = sorted(heights)
        return sum([c != h for c, h in zip(check, heights)])

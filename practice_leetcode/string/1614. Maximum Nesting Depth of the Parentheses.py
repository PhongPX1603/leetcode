class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max = 0
        for i in range(len(s) - 1):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count > max:
                max = count
        return max
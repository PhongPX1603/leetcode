class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        result = 0
        for i in range(len(s)):
            if s[i] == 'R':
                count += 1
            elif s[i] == 'L':
                count -= 1
            
            if count == 0:
                result += 1
        return result
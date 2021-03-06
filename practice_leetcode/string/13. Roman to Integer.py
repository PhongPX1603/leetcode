class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s) - 1):
            if table[s[i]] < table[s[i+1]]:
                result -= table[s[i]]
            else:
                result += table[s[i]]
        return result + table[s[-1]]
                
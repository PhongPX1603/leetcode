class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = defaultdict(int)
        for i, char in enumerate(order):
            result[char] = i
        
        return ''.join(sorted(s, key=lambda x: result[x]))
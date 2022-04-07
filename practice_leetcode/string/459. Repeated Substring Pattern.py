class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
# solotion 1: 5% faster, less 60% memory
        for i in range(1, n):
            if s.count(s[:i]) == n/len(s[:i]):
                return True
        return False

# solution 2: 40% faster, less 30% memory
        # for i in range(1, n):
        #     if n % len(s[:i]) == 0:
        #         count = 0
        #         check = s[:i]
        #         for j in range(0, n, i):
        #             if s[j: i + j] == check:
        #                 count += 1
        #             else:
        #                 break
        #         if count == n/len(s[:i]):
        #             return True
        # return False
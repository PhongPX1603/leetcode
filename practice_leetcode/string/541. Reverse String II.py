class Solution:
    def reverseStr(self, s: str, k: int) -> str:
#solotion 1: faster 40%, less 20% memory

        # s = list(s)
        # for i in range(0, len(s), 2*k):
        #     x = 0 + i
        #     y = min(x + k - 1, len(s) - 1)
        #     print(x, y)
        #     while x < y:
        #         s[x], s[y] = s[y], s[x]
        #         x += 1
        #         y -= 1
        # return ''.join(s)
        
#solution 2: same solution 1
        s = list(s)
        if len(s) < k:
            s = reversed(s)
        else:
            for i in range(0, len(s), 2*k):
                s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
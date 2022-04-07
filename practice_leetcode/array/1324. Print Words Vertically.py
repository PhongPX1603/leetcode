class Solution:
    def printVertically(self, s: str) -> List[str]:

# solution 1: faster than 40%, less than 25%
        result = []
        s = s.split()
        n = len(sorted(s, key=lambda x: len(x), reverse=True)[0])
        def myfunc(a, n):
            return a + ' ' * (n-len(a))
        s = list(map(myfunc, s, [n] * len(s)))
        for i in range(n):
            char = ''
            for j in range(len(s)):
                char += s[j][i]
            result.append(char.rstrip())
        return result
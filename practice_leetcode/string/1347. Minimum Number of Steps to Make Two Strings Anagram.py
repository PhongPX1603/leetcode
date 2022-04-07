class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        result = 0
        counter_s = Counter(s)
        counter_t = Counter(t)
        for c_s in counter_s:
            if c_s not in counter_t:
                result += counter_s[c_s]
            else:
                if counter_s[c_s] > counter_t[c_s]:
                    result += counter_s[c_s] - counter_t[c_s]
        return result
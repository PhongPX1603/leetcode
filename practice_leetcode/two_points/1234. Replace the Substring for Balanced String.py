class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        hashmap = {char: s.count(char) for char in ['Q', 'W', 'E', 'R']}
        
        extra = {}
        for k, v in hashmap.items():
            if v > n:
                extra[k] = v - n
                
        i, j = 0, 0
        res = len(s) + 1
        count = len(extra)
        
        if count == 0:
            return 0
        
        while j < len(s):
            if s[j] in extra:
                extra[s[j]] -= 1
                if extra[s[j]] == 0:
                    count -= 1
            if count == 0:
                while count == 0:
                    res = min(res, j-i+1)
                    if s[i] in extra:
                        extra[s[i]] += 1
                        if extra[s[i]] == 1:
                            count += 1
                    i += 1
                j += 1
            elif count > 0:
                j += 1
        return res
                
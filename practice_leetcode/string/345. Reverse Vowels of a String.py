class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        s = list(s)
        vow = {'a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U'}
        while i < j:
            if s[j] not in vow:
                j -= 1
            elif s[i] not in vow:
                i += 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
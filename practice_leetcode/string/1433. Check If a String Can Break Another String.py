class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        check_s1 = False
        check_s2 = False
        for i in range(len(s1)):
            if ord(s1[i]) > ord(s2[i]):
                check_s1 = True
            elif ord(s1[i]) < ord(s2[i]):
                check_s2 = True
        return check_s1 != check_s2
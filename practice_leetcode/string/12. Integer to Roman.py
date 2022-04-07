class Solution:
    def intToRoman(self, num: int) -> str:
        table = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        result = ''
        for i in reversed(range(len(str(num)))):
            check = num//(10**i)
            if check in range(1, 4):
                result += table[10 ** i] * check
            elif check == 4:
                result += table[10 ** i] + table[(10 ** i) * 5]
            elif check == 5:
                result += table[(10 ** i) * 5]
            elif check in range(6, 9):
                result += table[(10 ** i) * 5] + table[(10 ** i)] * (check - 5)
            elif check == 0:
                pass
            else:
                result += table[(10 ** i)] + table[10 ** (i+1)]
            num -= check * 10 ** i
        return result
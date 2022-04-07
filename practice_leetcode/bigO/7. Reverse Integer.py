class Solution:
    def reverse(self, x: int) -> int:
# solution 1: faster than 60%, less than 70% 
        # pos_reg = 1
        # if x < 0:
        #     x *= -1
        #     pos_reg = -1
        # k = 10 ** (len(str(x))-1)
        # result = 0
        # for _ in range(len(str(x))):
        #     du = x%10
        #     result += du * k
        #     k //= 10
        #     x = (x-du)//10
        # if (result < -2 ** 31 or result >= 2 ** 31) or (x < -2 ** 31 or x >= 2 ** 31):
        #     return 0
        # return result * pos_reg
        
# solution 2: same solution 1
        pos_reg = 1
        if x < 0:
            x = -x
            pos_reg = -1
        result = ''.join(reversed(list(str(x))))
        result = int(result)
        
        if (result < -2 ** 31 or result >= 2 ** 31) or (x < -2 ** 31 or x >= 2 ** 31):
            return 0
        return result * pos_reg
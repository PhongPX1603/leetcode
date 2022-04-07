class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            count = 0
            for i in reversed(range(len(digits))):
                if digits[i] == 9:
                    count += 1
                else:
                    break
            if count == len(digits):
                digits = [1] + [0] * count
            else:
                digits[-count:] = [0] * count
                digits[-count-1] = digits[-count-1] + 1
        return digits
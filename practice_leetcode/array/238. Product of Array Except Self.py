import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        k = 1
        for i in reversed(range(len(nums))):
            result[i] *= k
            k *= nums[i]

        return result
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        i, j = 0, 0
        res = 0
        if len(nums) <= k:
            return k
        while i < len(nums):
            if nums[i] == 0:
                count += 1
            i += 1
            while k < count:
                if nums[j] == 0:
                    count -= 1
                j += 1
            res = max(res, i-j)
        return res
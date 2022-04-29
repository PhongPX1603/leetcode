class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if num % 2 != 0 else 0 for num in nums]
        sums = {0: 1}
        curSum = 0
        res = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            res += sums.get(diff, 0)
            sums[curSum] = 1 + sums.get(curSum, 0)
        return res
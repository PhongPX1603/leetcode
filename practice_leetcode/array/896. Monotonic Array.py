class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
# solution 1: faster than 30%, less than 85%
        # increasing = False
        # decreasing = False
        # for i in range(len(nums) - 1):
        #     if nums[i] < nums[i + 1]:
        #         increasing = True
        #     elif nums[i] > nums[i + 1]:
        #         decreasing = True
        # return not(increasing and decreasing)

# solution 2:  faster than 85%, less than 60%
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)
        
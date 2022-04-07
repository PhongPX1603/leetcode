class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
#solution 1: 
        nums.sort()
        result = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                result.append(nums[i])
        return result
    
#solution 2: same solution 1
        # result = []
        # for num in nums:
        #     if nums[abs(num) - 1] > 0:
        #         nums[abs(num) - 1] *= -1
        #     else:
        #         result.append(abs(num))
        # return result
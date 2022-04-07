class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#solution 1: faster than 30%, less than 95%
        # result = []
        # for i, num in enumerate(nums):
        #     if target - num in (nums[:i] + nums[i+1:]):
        #         result.append(i)           
        # return result
    
#solution 2: faster than 35%, less than 96%
        # result = []
        # for i, num in enumerate(nums):
        #     if target - num in (nums[i+1:]):
        #         result.append(i)
        #         second = nums[i+1:].index(target-num) + i + 1
        #         result.append(second) 
        # return result
    
#solution 3: faster than 65%, less than 50%
        seen = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [i, seen[rem]]
            seen[num] = i
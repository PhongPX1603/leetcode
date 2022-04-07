class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#solution 1: faster than 75%, less than 7%
        # return list(set(range(len(nums) + 1))-set(nums))[0]   #or
        # return sum(range(len(nums) + 1)) - sum(nums)

#solution 2: faster than 35%, less than 7%
        # i = 0
        # nums.sort()
        # while i < len(nums):
        #     if i != nums[i]:
        #         return i
        #     else:
        #         i += 1
                
#solution 3: hash table - same solution 1
        table = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            table[nums[i]] = 1
        return table.index(0)
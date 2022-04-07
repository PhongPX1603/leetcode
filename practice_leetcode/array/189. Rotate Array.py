class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#solution 1: faster than 15%, less than 80%
        # n = len(nums)
        # nums.reverse()
        # for i in range(k):
        #     check = nums.pop(0)
        #     nums.append(check)
        #     # check = nums.pop()    can replace by 2 these lines and don't need to use reverse() func
        #     # nums.insert(0, check)
        # nums.reverse()
        
#solution 2: faster than 90%, less than 80%
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
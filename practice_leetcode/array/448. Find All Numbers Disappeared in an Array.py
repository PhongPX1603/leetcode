class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all_nums = set(range(1, len(nums) + 1))
        result = list(all_nums - set(nums))
        return result
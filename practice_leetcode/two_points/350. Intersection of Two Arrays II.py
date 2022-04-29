class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
# solution 1: faster than 60%,  less than 50%
        # i, j = 0, 0
        # res = []
        # nums1.sort()
        # nums2.sort()
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] > nums2[j]:
        #         j += 1
        #     elif nums1[i] < nums2[j]:
        #         i += 1
        #     else:
        #         res.append(nums1[i])
        #         i += 1
        #         j += 1
        # return res
    
# solution 2: speed and memory like solution 1
        nums1_di = {}
        res = []
        for num in nums1:
            if num not in nums1_di:
                nums1_di[num] = 1
            else:
                nums1_di[num] += 1
        for num in nums2:
            if num in nums1_di and nums1_di[num]:
                res.append(num)
                nums1_di[num] -= 1
        return res
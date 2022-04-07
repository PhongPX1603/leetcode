class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = set(nums)
        dic = {}
        for ele in elements:
            count = 0
            for i in nums:
                if ele == i:
                    count += 1
            dic[ele] = count
        return sorted(dic.items(), key=lambda item: item[1])[-1][0]
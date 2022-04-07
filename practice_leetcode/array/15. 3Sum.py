class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

# solution 1: faster than 8%
        # n = len(nums)
        # if n < 3:
        #     return []
        # nums.sort()
        # result = []
        # for i in range(n-2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     j = i + 1
        #     k = n - 1
        #     while j < k:
        #         if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in result:
        #             result.append([nums[i], nums[j], nums[k]])
        #             k -= 1
        #         elif nums[i] + nums[j] + nums[k] < 0:
        #             j += 1
        #         else:
        #             k -= 1
        # return result

#solution 2: faster than 95%
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            supplements = set()
            results = []
            for num in nums:
                if target - num not in supplements:
                    supplements.add(num)
                else:
                    results.append([num, target - num])
            return results

        nums = sorted(nums)
        n = len(nums)
        results = set()

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:  # already scanned through
                continue

            pairs = twoSum(nums=nums[i + 1 : n], target=-nums[i])
            if len(pairs) > 0:
                for pair in pairs:
                    if (nums[i], pair[1], pair[0]) not in results:
                        results.add((nums[i], pair[1], pair[0]))
        return [list(r) for r in list(results)]
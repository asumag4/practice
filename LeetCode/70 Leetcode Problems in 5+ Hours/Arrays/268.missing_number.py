# Beats 100%

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        def less_than_target(x):
            if x <= target:
                return x
            else:
                return
        
        filtered_nums = list(filter(less_than_target, nums))
        filtered_nums.sort()
        # print(filtered_nums)

        for j, n in enumerate(filtered_nums):
            for k, m in enumerate(filtered_nums[j+1:]):
                if ((n + m) == target):
                    return [nums.index(n), nums.index(m)]

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))
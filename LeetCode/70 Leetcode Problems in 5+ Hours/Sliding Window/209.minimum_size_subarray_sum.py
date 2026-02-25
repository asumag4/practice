class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        if target in nums:
            return 1
        
        if sum(nums) == target:
            return len(nums)

        
        
        k = 2
        
        while (k < len(nums)):
        
            i = 0

            while (i <= len(nums) - k):

                print(nums[i:i+k])
                if sum(nums[i:i+k]) == target:

                    

                    return len(nums[i:i+k])
                i += 1

            k += 1

        return 0

sol = Solution()
# print(sol.minSubArrayLen(53, [1, 3, 9, 10, 13, 16, 17, 20]))
print(sol.minSubArrayLen(11, [1,2,3,4,5]))
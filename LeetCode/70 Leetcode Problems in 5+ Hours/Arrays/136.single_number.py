class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        numsLen = len(nums)
        # Base case
        if numsLen == 1:
            return nums[0]
        
        # Init a `seen`
        seen = set()

        # Order the list
        nums.sort()

        # Go through the entire list
        for i, n in enumerate(nums):
            # If number not in `seen` and the next number is different; then that's the one that doesn't appear twice
            if (n not in seen):
                seen.add(n)
                if ((i == numsLen - 1) or (nums[i+1] != n)): # Need to handle edge case of the last number being the singular element
                    return n

sol = Solution()
print(sol.singleNumber([4,1,2,1,2])) # 4
print(sol.singleNumber([2,2,1])) # 1
print(sol.singleNumber([1])) # 1
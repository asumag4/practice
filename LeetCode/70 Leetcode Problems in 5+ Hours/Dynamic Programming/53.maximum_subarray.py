class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Have reference vars
        tot = 0
        maxSub = nums[0]

        # Go through each int
        for i in nums:

            # print(f"At: {i}, Tot: {tot}, maxSub {maxSub}") # DEBUG

            if tot < 0:
                tot = 0
            
            tot += i
            maxSub = max(maxSub, tot)

        return maxSub

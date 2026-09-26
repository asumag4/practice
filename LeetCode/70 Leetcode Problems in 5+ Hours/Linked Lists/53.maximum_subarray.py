class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Two-pointer solution
        numsLen = len(nums)

        # Base case 
        if (numsLen == 1):
            return nums[0]

        a = 0
        b = 0
        curr_sum = sum(nums[a:b])
        maxSubArray = sum(nums)

        while (b < numsLen) :

            new_sum = sum(nums[a:b+1])
            # print(nums[a], nums[b], new_sum) # DEBUG

            if (new_sum > maxSubArray):
                maxSubArray = new_sum
            
            if (new_sum >= curr_sum):
                b += 1
            elif (new_sum < curr_sum):
                a += 1
                if a > b:      # never let the window go empty
                    b = a

        # while (a <= numsLen):
        #     new_sum = sum(nums[a:b+1])
        #     if (new_sum > maxSubArray):
        #         maxSubArray = new_sum
        #     a += 1
            
        
        return maxSubArray
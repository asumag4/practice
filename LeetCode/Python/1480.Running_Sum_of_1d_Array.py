"""
Given an array nums. 

We define a running sum of an array as 
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

# --- MY SOLUTION ---

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSumLst = []
        runningSumInt = 0 
        for i in nums:
            runningSumInt += i
            runningSumLst.append(runningSumInt)
        return runningSumLst
    
# --- BEST SOLUTION --- 

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix_sum = [nums[0]] # Intialize the first step 
        for i in range(1, len(nums)):  
            prefix_sum.append(nums[i] + prefix_sum[-1])
        return prefix_sum
    

# --- TESTING --- 

solution = Solution() 
print(solution.runningSum([1,2,3,4])) # [1,3,6,10]
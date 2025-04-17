"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

# --- MY SOLUTION ---

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # This is a simple binary search, test cases seem to exclude 
        # any form of repetition in the input lists 

        # The test-cases are also sorted, assume all tests are sorted

        # Determine if list != empty
        if nums:
            lo = 0
            hi = len(nums) - 1
            while (lo <= hi):
                mid = (hi + lo) // 2  
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid - 1
                else: 
                    lo = mid + 1
        return -1 
    
# --- BEST SOLUTION --- 
class Solution: 
    def search(self, nums: list[int], target: int) -> int:
        i = 0 # Set the lower bound
        j = len(nums)-1 # Set the upper bound
        while i <= j: # While the lower bound is lower or equal to the upper bound
            m = (i+j)//2 # Find the middle of the 
            if nums[m] == target: # If the middle value == target 
                return m # Return the index of middle value
            elif nums[m] > target: 
                j = m-1
            else:
                i = m+1
        return -1

# --- TEST CASES ---

solution = Solution()

# LC Testcase 
print(solution.search([-1,0,3,5,9,12], 9)) # 4 
print(solution.search([-1,0,3,5,9,12],2)) # -1 
print(solution.search([-1,0,3,5,9,12], 13)) # -1 

# Only one item
print(solution.search([-1],-1)) # 0 

# No items 
print(solution.search([],-1)) # -1

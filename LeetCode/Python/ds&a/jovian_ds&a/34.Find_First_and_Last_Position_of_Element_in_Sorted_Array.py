
class Solution:
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def binarySearchLimits(nums, target, lower): # We'll toggle between the lower and upper bounds 

            lo = 0
            hi = len(nums) - 1

            while lo <= hi: 

                mid = (hi + lo) // 2
                    
                if nums[mid] == target:
                    # If we're looking for the lower bound in a sorted list: 
                    if lower and (nums[mid-1] < target): 
                        return mid
                    
                    # If we're looking for the upper bound in a sorted list:
                    elif (not lower) and (nums[mid+1] > target):
                        return mid
                
                # If we we're not finding the range of targets; then keep searching

                elif nums[mid] < target: 
                    # Shift left 
                    hi = mid - 1
                else: 
                    # Shift right 
                    lo = mid + 1 
            
            return -1

        return binarySearchLimits(nums, target, True), binarySearchLimits(nums, target, False)


        # Then look if +/- position 

# --- BEST SOLUTION --- 
            

# --- TEST CASES ---

solution = Solution()

print(solution.searchRange([5,7,7,8,8,10], 8)) # 3,4 
print(solution.searchRange([5,7,7,8,8,10], 6)) # -1,-1

# Edge cases

# What if theres triplicates instead of duplicates? 
print(solution.searchRange([1,1,2,2,2,3,4,5,7,7,8,8,8,10], 8)) # 10,11
print(solution.searchRange([1,1,2,2,2,3,4,5,7,7,8,8,8,10], 2)) # 2,3

print(solution.searchRange([1,1,2,2,2,2,2,2,2,2,2,3,4,5,7,7,8,8,8,10], 2)) # 2,3
      
# What if theres more? 
      
# What if the targets are on the start and end of the array? 
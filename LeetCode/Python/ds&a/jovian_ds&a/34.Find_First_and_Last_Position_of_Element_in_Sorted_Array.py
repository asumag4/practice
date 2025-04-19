class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        # Binary search for the first occurance of 8 
        lo = 0 
        hi = len(nums) - 1 

        for _ in range(len(nums)):

            mid = (hi + lo) // 2

            # print(f"lo: {nums[lo]}")
            # print(f"hi: {nums[hi]}")
            # print(f"mid: {nums[mid]}")
            # print(f"range: {nums[lo:hi+1]}")

            if nums[mid] == target: 

                # We then need to implement how we can find the first and second instance of our target! 
                while nums[mid-1] == target: 

                    mid = (hi + lo) // 2

                    if nums[mid-1] != target: # If we're at the first instance
                        return [mid, mid+1]
                    elif nums[mid-1] == target: # If going down gets us closer to our target
                        print("Going left")
                        hi = mid - 1 
                    else: # Going higher gets us closer to our target
                        print("Going right")
                        lo = mid + 1
                
            
            elif nums[mid] > target: 
                # print("Going left")
                hi = mid - 1
            
            else: 
                # print("Going right")
                lo = mid + 1 
        
        return [-1, -1]

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
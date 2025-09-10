class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Start the binary search
        lo = 0 
        hi = len(nums) - 1

        # Init a while loop if lo and hi positions stil make sense
        while (lo <= hi):

        # Calc the mid 
            mid = (lo + hi) // 2

            # Assess if were at the target, then return mid 
            if (nums[mid] == target):
                return mid
            
            # Now we need to find the range we need to look for 

            # If the lo to mid portion is organized, then;
            elif (nums[lo] <= nums[mid]):
                # See if the target is within that range; if so go left
                if (nums[lo] <= target <= nums[mid]):
                    hi = mid - 1
                # If not then go right
                else:
                    lo = mid + 1
            
            # If the mid to hi portion is organized, then;
            elif (nums[mid] <= nums[hi]):
                # See if the target is within that range; if so go right
                if (nums[mid] <= target <= nums[hi]):
                    lo = mid + 1
                # If not then go left
                else:
                    hi = mid - 1
        
        # If not found the terminate then wait until while loop terminates and return -1 
        return -1
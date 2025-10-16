class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        # We're gonna have to use another function that has directionality 
        def binary_search_directional(nums, target, searching_left):
            
            lo = 0 
            hi = len(nums) - 1
            idx = -1

            # Setup the binary search 
            while (lo <= hi):

                mid = (hi + lo) // 2
            # If mid number is greater than the target; go left 
                if (nums[mid] > target):
                    hi = mid - 1
            # elif the mid number is less than the target; go right 
                elif (nums[mid] < target):
                    lo = mid + 1
            # now if we found the number already -> look for the edge 
                else:
            # if were looking left, go left
                    if (searching_left):
                        hi -= 1
                        idx = mid
            # else go right 
                    else:
                        lo += 1
                        idx = mid

            return idx

        left = binary_search_directional(nums = nums, target = target, searching_left = True)
        right = binary_search_directional(nums = nums, target = target, searching_left = False)
        return [left, right]
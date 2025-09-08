class Solution:
    def search(self, nums: list[int], target: int) -> int:
            # We need to levarage the values of high and min=
            # When lo > hi, we've found a critical point
            
            lo = 0
            hi = len(nums) - 1
            # idx = -1

            # print(lo) # DEBUG
            # print(hi) # DEBUG
            if (not nums):
                return -1
            
            # We also need to leverage the the +1 and -1 values of the middle position 
            while (lo <= hi):
                
                mid = (hi + lo) // 2
                
                print(nums[lo]) # DEBUG
                print(nums[mid]) # DEBUG
                print(nums[hi]) # DEBUG

                if (hi == lo):
                    if ((nums[hi] == target) and (nums[lo] == target)):
                        return mid
                    else:
                        return -1

                elif (nums[mid] == target):
                    return mid
                
                # If target is within lo -> mid-1, go lower 
                elif ( (nums[lo] <= target) and (nums[mid-1] >= target) ):
                    hi = mid - 1 

                # If target is within mid+1 -> hi, go higher 
                elif ( (nums[mid+1] <= target) and (nums[hi] >= target) ):
                    lo = mid + 1

                else:
                    return -1
            
sol = Solution()
# print(sol.search([4,5,6,7,0,1,2], 0))
# print(sol.search([1,2,3,4,5,6,7,8,9,10], 3))
# print(sol.search([6,7,8,9,10,1,2,3,4,5], 3))
# print(sol.search([3,4,5,1,2,3], 3))
# print(sol.search([1,2,5,6,7], 7))
# print(sol.search([1,2,5,6,7], 7))
# print(sol.search([4,5,6,7,0,1,2], 3))
# print(sol.search([3,4,5,1,2,3], 6))
# print(sol.search([1,2,3,4,5,6,7,8,9,10], -1))

print(sol.search([1,3], 2))
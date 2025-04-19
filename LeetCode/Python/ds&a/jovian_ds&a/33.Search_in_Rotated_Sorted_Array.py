# -- Binary Search Method -- 

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        nums_len = len(nums)
        
        for _ in range(nums_len):

            mid = (hi + lo) // 2 

            # print(f"lo: {nums[lo]}")
            # print(f"hi: {nums[hi]}")
            # print(f"Mid: {nums[mid]}")
            # print(f"Range: {nums[lo:hi+1]}")

            # First assess if the middle numbers is the target number 
            if nums[mid] == target: 
                return mid

            # Handling if the lo and hi are the targets!
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi

            # Determine if the mid value is a pivotal point 

            if (mid+2 <= (nums_len - 1)) and (mid-2 >= 0): # Only assess this when we can still be in range
                if nums[mid-2] > nums[mid+2]:
                    # Shift left if its closer to the target number 
                    if (abs(((nums[mid-2]+nums[mid-1])/2) - target)) < abs(((nums[mid+1]+nums[mid+1])/2 - target)):
                        hi = mid - 1

                    # Shift right if its closer to the target number 
                    else: 
                        lo = mid + 1

                # If not a mid value; conduct regular binary search
                elif nums[mid] > target: 
                    hi = mid - 1
                else: 
                    lo = mid + 1

        return -1 

# --- TEST CASES --- 

solution = Solution()

print(solution.search([4,5,6,7,0,1,2], 0)) # 4

print(solution.search([4,5,6,7,0,1,2], 3)) # -1

print(solution.search([1], 0)) # -1

print(solution.search([1,3], 3)) # 1

print(solution.search([1], 1)) # 0

print(solution.search([3,4,5,6,1,2], 2)) # 5

print(solution.search([4,5,6,7,8,9,1,2,3], 1)) # 6

print(solution.search([4,5,6,7,8,1,2,3], 8)) # 4
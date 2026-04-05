class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Determine the high and lower positions 
        lo = 0
        hi = len(nums) - 1
        
        # While the lower < higher position 
        while (lo <= hi): # **Needs to have an 'equals to' condition
        
        # Determine the mid point 
            mid = (hi + lo) // 2 # **We add it up so that the mid is calculated correctly

            print(nums[lo : hi])
            print(mid)
        # If the mid point is the target, return target
            if (nums[mid] == target):
                return mid
        # If the position of the next position is less than the target value,
        # the mid point is too low, so increase the lower position by 1 
            elif (nums[mid] < target): # **We look at the middle point, and see where we need to go
                lo += 1
            else:
                hi -= 1
        return -1 # **When while loop doesn't find the answer, we return -1
        # Vice versa



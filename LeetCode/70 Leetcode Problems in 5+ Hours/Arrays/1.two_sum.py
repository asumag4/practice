class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        traversed = {}

        # Traverse all the numbers
        for i, val in enumerate(nums):
        
            # For each number, check if the number exists in the
            diff = target - val
            if (diff in traversed.keys()):
                return [i,traversed[diff]]
            traversed[val] = i 
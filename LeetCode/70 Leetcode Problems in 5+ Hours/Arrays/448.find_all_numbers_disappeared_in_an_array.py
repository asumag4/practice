# Beats 86.41%

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(list(range(len(nums)+1))) - sum(nums)
    
    # Solution is O(N) -> input size is linearly related to the generation of the 
    # "expected"/"correct" list without missing numbers
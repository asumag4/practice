class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        idx_tabulator = {}
 
        for idx, val in enumerate(nums):
            diff = target - val

            if diff in idx_tabulator.keys():
                return [idx_tabulator[diff], idx]
            
            idx_tabulator[val] = idx
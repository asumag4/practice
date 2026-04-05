class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        recorder = {}
        
        for num in nums: 
            if num not in recorder.keys():
                recorder[num] = True 
            else: 
                return True 

        return False
    
# ======= BEST SOLUTION =======

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        return True
    

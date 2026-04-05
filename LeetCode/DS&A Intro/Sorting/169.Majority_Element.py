# ========= MY SOLUTION ===================
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        uniq = set(nums)
        counter = { i: 0 for i in nums}
        # print(counter) # DEBUG

        for i in nums:
            counter[i] += 1
        # print(counter) # DEBUG

        n = len(nums) / 2
        # print(n) # DEBUG
        
        for i, j in counter.items():
            if j > n:
                return i 
            
# ========= BEST SOLUTION========= 
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        res = hp = 0

        for x in nums:
            if hp == 0:
                res=x
                hp=1
            else:
                hp+=1 if res == x else -1
        return res

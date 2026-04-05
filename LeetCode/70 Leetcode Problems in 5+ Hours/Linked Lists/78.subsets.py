class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        def dfs(sub = None, idx = 0):

            if (sub == None):
                sub = []
            
            if (idx == len(nums)):
                res.append(sub[:])
                return
            else:
                sub.append(nums[idx])
                dfs(sub[:], idx + 1)

                sub.pop()
                dfs(sub[:], idx + 1)
    
        res = []
        dfs()
        return res
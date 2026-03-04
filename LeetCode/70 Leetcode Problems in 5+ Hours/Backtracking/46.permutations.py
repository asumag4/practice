class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        res = []

        def recurse(subset, window):
            print(subset, window)
            if (len(subset) == len(nums)) and (len(window) == 0):
                res.append(subset)
                return
            else:
                
                for n in window:
                    subset_c = subset.copy()
                    window_c = window.copy()

                    subset_c.append(n)
                    recurse(subset, window_c.remove(n))
                    subset_c.pop()
            
        for n in nums:
            subset = [n]
            window = nums.copy()
            window.remove(n)
            recurse(subset, window)

sol = Solution()
print(sol.permute([1,2,3]))
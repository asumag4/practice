class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        def recursion(subset, window):
            # If we are at the end of the list `nums`
            if len(window) == 1:
                subset = subset.append(window)
                res.add(subset)
                return
            else:
                print(f"{subset}, {window}")
                subset = subset.append(window[1])
                res.add(subset)
                for i, _ in enumerate(window):
                    recursion(subset, window[i:])

        res = set([])
        
        for i, n in enumerate(nums):
            # print(f"{i[]}, {nums[i:]}")
            recursion([i], nums[i:])
        
        return res

sol = Solution()
print(sol.subsets([1,2,3]))

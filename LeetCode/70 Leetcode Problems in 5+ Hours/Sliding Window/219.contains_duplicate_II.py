# Beats 5%

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        hmap = {}

        for i, n in enumerate(nums):

            print(f"{i},{n}")

            if n in hmap:
                return True
            else:
                hmap[n] = i
            
            if (i + 1) > k:
                first_key = next(iter(hmap))
                del hmap[first_key]
        
        return False
    
sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
            
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
    
sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
            
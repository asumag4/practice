class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        for i, num in enumerate(nums):

            if num in nums[i+1:]:
                print(f"Found {num} in {nums[i+1:]}")
                j = nums[i+1:].index(num)
                j += i + 1
                if abs(i-j) <= k:
                    print(i, j)
                    return True
                else:
                    continue
    
sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
            
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        i = 0
        j = 1

        while (
            i <= len(nums) - 2 and
            j <= len(nums) - 1
        ):
            while (j <= (len(nums) - 1)):

                if (nums[i] == nums[j]):

                    if (abs(i - j) <= k):
                        return True
                    else: 
                        i += 1
                        j = i + 1
                    
                else: 
                    j += 1
            
            i += 1
            j = i + 1
        
        return False
    
sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
            
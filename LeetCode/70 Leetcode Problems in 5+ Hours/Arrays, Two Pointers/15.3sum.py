class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i in range(0, len(nums)):
            
            if (i < 0) and (nums[i] == nums[i-1]):
                continue
            
            j = i + 1
            k = len(nums) - 1

            while (j < k):

                case = nums[i] + nums[j] + nums[k]

                if (case > 0):
                    k -= 1
                elif (case < 0):
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1

                    while (j < k) and (nums[j] == nums[j-1]):
                        j += 1

        return res
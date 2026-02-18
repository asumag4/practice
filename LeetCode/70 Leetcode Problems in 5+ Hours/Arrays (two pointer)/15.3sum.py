class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        i = 0
        j = 1
        k = 2
        arr_len = len(nums)
        nums.sort()
        output = []

        # print(nums[arr_len - 3])
        # print(nums[arr_len - 2])
        # print(nums[arr_len - 1])

        while (
            i <= (arr_len - 3) and
            j <= (arr_len - 2) and
            k <= (arr_len - 1)):

            # Iterate through j -> when j == len(nums) - 2, then reset
            while (j <= arr_len - 2):
         
                # Iterate through k -> when k == len(nums) - 1, then reset
                while (k <= (arr_len - 1)):

                    print(f"{nums[i]}, {nums[j]}, {nums[k]}") # DEBUG

                    # See if k < (arr_len - 1)
                    if ((nums[i] + nums[j] + nums[k]) == 0):
                        if ([nums[i], nums[j], nums[k]] in output):
                            continue 
                        else:
                            output.append([nums[i], nums[j], nums[k]])
                        # Jump j when we've found a sum of 0 in this iteration of i & j
                        i += 1
                        j = i + 1

                    k += 1
                
                j += 1
                k = j + 1

                # Jump i when we've found a sum of 0 in this iteration of i
                if ((nums[i] + nums[j] + nums[k]) >= 0):
                    i += 1
                    j = i + 1
                    k = j + 1
            
            i += 1
            j = i + 1
            k = j + 1

        return output

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# [-4, -1, -1, 0, 1, 2]
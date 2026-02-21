# Beats 76.96%

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
#         hmap = {}

#         nums_sorted = sorted(nums)

#         for idx, i in enumerate(nums_sorted):
#             if i not in hmap.keys():
#                 hmap[i] = idx

#         return [hmap[i] for i in nums]
    
# ===================================
# Top solution:
# ===================================

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count=[0]*101 # Using known restriction of inputs to generate a long list of 0's
        for num in nums:
            count[num]+=1
        print(count)
        for j in range(1, 101):
            # print(f"For j = {j}, value = {j-1}")
            count[j]+=count[j - 1]
        print(count)
        return [0 if num==0 else count[num-1] for num in nums]


sol = Solution()
# print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
sol.smallerNumbersThanCurrent([8,1,2,2,3])
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        hmap = {}

        nums1 = sorted(nums)

        for i in nums1:
            num = nums1.pop()
            hmap[num] = len()            

sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
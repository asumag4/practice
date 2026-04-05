"""
Example 1: 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3: 
Input: nums = [0,0,0]
Output: [[0,0,0]]

Example 4: 
Input: nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
Output: [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]

Example 5:
Input: nums = [1,-1,-1,0]
Output: [[-1,0,1]]
"""

class Solution():

    def threeSum(self, nums): 
        
        # Initiate the sorted list of 
        nums.sort()
        # Initate a blank list as a response
        res = []

        # Iterate through the positions in `nums`
        for i in range(len(nums)):
            # Skip a step if we're greater than the first position, but the previous pos holds the same value as the current pos
            if (i > 0 and (nums[i] == nums[i-1])):
                continue

            # Make the left anchor the following pos
            left = i + 1
            # Make the right anchor the last pos
            right = len(nums) - 1

            # Keep iterating as the left pos is less than the right pos
            while left < right:
                # Hold your current `3 sum`
                s = nums[i] + nums[left] + nums[right]

                # If your sum is 0
                if (s == 0): 
                    # Append it in the response 
                    res.append([nums[i], nums[left], nums[right]])
                    # Iterate your left and right anchors to go +1 and -1 respectively (squish in)
                    left += 1
                    right -= 1
                    # Have another loop, while the iterations are still valid and if the left anchor is the same value as the previous left anchor 
                    while ((left < right) and (nums[left] == nums[left - 1])):
                        # Keep going left (avoid duplicates)
                        left += 1
                    # Same logic on the right (avoid duplicates)
                    while ((left < right) and (nums[right] == nums[right + 1])):
                        right -= 1
        
                # if the sum is less than 0, go right on your left anchor 
                elif (s < 0): 
                    left += 1
                # else, go opposite
                else: 
                    right -= 1

        return res
        # return your response
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,1,1]))
print(sol.threeSum([0,0,0]))
# print(sol.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
# print(sol.threeSum([1,-1,-1,0]))
# print(sol.threeSum([0,0,0,0]))
# print(sol.threeSum([-2,0,1,1,2]))
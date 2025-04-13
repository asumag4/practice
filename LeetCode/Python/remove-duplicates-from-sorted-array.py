# def removeDuplicates(nums: list[int]) -> int:
#     # Iterate through the list
#     i = 0 
#     while i < (len(nums)-1): 
#         if nums[i] == nums[i+1]:
#             nums.pop(i)
#         else: 
#             i += 1 
#     return nums 

##### BETTER SOLUTION ####

def removeDuplicates(nums: list[int]) -> int: 
    # NOTE: init a counter variable
    x = 0 
    for i in range(1, len(nums)):
        # If the first value you count (x) doesn't equal to the current iteration (i)....
        if nums[i] != nums[x]:
            # Move up on the value you first count
            x += 1
            # Make the value you first count (x) equal to the value of the current iteration; so that you keep skipping over subsequent equal values until you arrive to a different one 
            nums[x] = nums[i]
            print(nums)
    return x + 1 

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
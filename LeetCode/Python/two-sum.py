def recursiveSearch( nums: list[int], target: int, recurssionCount: int) -> list[int]: 

    # 1. Create an empty dictionary: num_to_index that will store numbers as keys and their indices as values
    # This will be used to quickly check if a complement exists 
    num_to_index = {}
    # 2. Iterate through the list 
    for i, num in enumerate(nums):
        # 3. Calculate the complement
        c = target - num
        # 4. Check if complement is already in the dictionary 
        if c in num_to_index:
            # 5. Return the indices of these two numbers as a list
            return [num_to_index[c], i]
        # 6. Update the dictionary if complement not in dictionary, ensuring that future iterations can find it as a complement if needed
        num_to_index[num] = i

# CASES 
print("First Case: ")
print(recursiveSearch([3,2,3], 6, 0))
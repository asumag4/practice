class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # We'll hold a base-case, if we have an empty string or string == None, then return 0
        if ((s == "") or (s == None)):
            return 0
       
        # We'll use a hashmap iteration for this solution
        # Grab the distinct characters within the string 
        count_chars = {char : 0 for char in s}
        # print(count_chars)

        # Initialize the first and last positions we are traversing through the string 
        first = 0 
        last = 0

        # Grab the len() of the string, the returned value from the function (we'll use it to our advantage)
        len_of_str = len(s)

        # Init max = 0
        max_len = 0 

        # While last < len() of the string 
        while (last < len_of_str):
            
            # Tabulate the first character in your dictionary 
            count_chars[s[last]] += 1

            # If for any of the values in the dictionary is greater than 1; then 
            if (any(x > 1 for x in list(count_chars.values()))):
                count_chars[s[first]] -= 1
                first += 1

            # Then grab the maximum length, between the current max or the current traversal length
            max_len = max(max_len, last - first + 1)
            # At the last step, move the last character 
            last += 1

        # Return max
        return max_len

# ====== BEST SOLUTION ====== 

class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int: 
        # Declare your return value
        # Declare the left 
        # Declare a hashmap (to track of counts)
        # Use a for loop, keeping track of the index per iteration as well
            # If a character is in the hasmap and the character position is greater than the left position 
                # set the left to be the position of that character + 1 
            # Then, for the character we are on; set it's value to the position we are on 
            # Grab the max between current max and from right_most - current_pos + 1
        # Return the answer
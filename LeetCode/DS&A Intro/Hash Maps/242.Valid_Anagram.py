class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Have your base case, but in this scenario if the lengths aren't the same 
        # you can immediately conclude they aren't Anagrams
        if (len(s) != len(t)):
            return False

        # Start a recorder 
        recorder = {}

        # Iterate through s and record each letter and it's occurance 
        for char in s:
            recorder[char] = recorder.get(char, 0) + 1

        # ITerate through t and see if a letter is not in s or is 0 (theres an extra letter in t)
        for char in t:
            if ((char not in recorder) or (recorder[char] == 0)):
                return False
            recorder[char] -= 1

        # If it passes all that, then return True
        return True
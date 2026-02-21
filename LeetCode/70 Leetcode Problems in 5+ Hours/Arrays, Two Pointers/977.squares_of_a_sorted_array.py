# Beats 100%

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([num**2 for num in nums])
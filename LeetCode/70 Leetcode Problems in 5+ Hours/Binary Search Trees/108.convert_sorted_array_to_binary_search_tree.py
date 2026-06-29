# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:

        # Base Case
        if (not nums):
            return 

        nums_len = len(nums)

        # When leaf is returned
        if (nums_len == 1):
            return TreeNode(val = nums[0], left = None, right = None)
        
        # Edge-case: for when theres only 2
        if (nums_len == 2):
            left_child = TreeNode(val = nums[0], left = None, right = None)
            parent = TreeNode(val = nums[1], left = left_child, right = None)
            return parent

        # Split
        parent_node_pos = len(nums) // 2
        # Assign left and right
        left_nums = nums[:parent_node_pos]
        right_nums = nums[parent_node_pos+1:]

        # Call sortedArrayToBST on left and right for remaining nodes 
        left = self.sortedArrayToBST(left_nums)
        right = self.sortedArrayToBST(right_nums)

        parent = TreeNode(nums[parent_node_pos], left = left, right = right)
        return parent
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Have a placeholder for the maximum length 
        diameter = 0

        # Call a recursive function that accepts a node + the depth
        def measure(node):
        
            # If there is no root, means the previous node was the leaf node, return the depth you're at
            if (not node):
                return 0

            # Get the depths of the left and right
            # For each iteration of the call, go (node.direction, depth + 1)
            left = measure(node.left)
            right = measure(node.right)

            # Get the max; are we getting higher values from our current diameter... or from the current left and right? 
            nonlocal diameter
            diameter = max(diameter, left + right)
            print(diameter) # DEBUG

            # After we've set the current highest measured diameter, return the longest recorded depth in either direction, +1 to account for the current node
            return max(left, right) + 1
        
        measure(root)
        return diameter

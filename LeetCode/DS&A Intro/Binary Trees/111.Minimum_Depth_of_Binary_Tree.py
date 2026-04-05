# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # Base case 
        if (not root):
            return 0

        # Determine an algorithm that finds the end of a node first 
        # Use the stack method
        stack = [(root, 1)]

        # Go through the stack; while theres still elements in it
        while (stack):
            
            node, depth = stack.pop(0) # Retrieve the first item in the stack

        # If the node does not exist, then return the depth
            if (not node):
                return depth
        # If there is no left side or right side on the current node you're on a leaf, return the depth
            if ((not node.left) and (not node.right)):
                return depth

        # If there is a left side, call the function again on the left side, +1 depth 
            if (node.left):
                stack.append((node.left, depth + 1))
        # If there is a right side, call the function again on the right side, +1 depth
            if (node.right):
                stack.append((node.right, depth + 1))

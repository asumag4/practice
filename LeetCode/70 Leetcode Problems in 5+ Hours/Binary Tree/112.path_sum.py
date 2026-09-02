# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # Employ DFS

        if (not root): return False

        if ((root.val == targetSum) and (not root.left) and (not root.right)): return True

        left, right = False, False
        if (root.left):
            left = self.hasPathSum(root.left, targetSum - root.val)
        if (root.right):
            right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # From every node you need to determine the length

        # Hold a global result value 
        res = 0

        def _traverse(node):

            nonlocal res

            if (not node):
                return 0

            left = _traverse(node.left)
            right = _traverse(node.right)

            res = max(res, left + right)

            return max(left+1,right+1)

        _traverse(root)
        return res

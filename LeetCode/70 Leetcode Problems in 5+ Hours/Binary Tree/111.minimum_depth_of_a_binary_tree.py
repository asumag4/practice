# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 1

        if (not root):
            return 0
        
        if ((root.left == None and (root.right) == None)):
            return res

        def dfs(node, depth): 
            if (node.left == None) and (node.right == None):
                return depth
            
            left = None
            right = None
            if node.left:
                left = dfs(node.left, depth + 1)
            if node.right:
                right = dfs(node.right, depth + 1)
            
            if not right: 
                return left
            elif not left:
                return right
            else:
                return min(left, right)
        
        res = dfs(root, res)
        return res
            
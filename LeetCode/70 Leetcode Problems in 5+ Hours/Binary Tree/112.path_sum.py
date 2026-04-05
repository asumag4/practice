# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def addChildNodes(node, total):

            if (node == None):
                return False

            tot = total - node.val
            
            if (tot == 0) and (node.left == None) and (node.right == None):
                return True
            elif (tot < 0):
                return False
            else:
                return addChildNodes(node.left, tot) or addChildNodes(node.right, tot)
        
        return addChildNodes(root, targetSum)
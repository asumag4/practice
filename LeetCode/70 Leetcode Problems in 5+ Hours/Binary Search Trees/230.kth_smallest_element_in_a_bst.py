# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Do inorder traversal
        self.vals = []

        def inOrderTraverse(node):

            if (not node):
                return 
            
            inOrderTraverse(node.left)
            self.vals.append(node.val)
            inOrderTraverse(node.right)

            return 
        
        inOrderTraverse(root)
        print(self.vals)
        return self.vals[k-1]
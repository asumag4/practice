# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.vals = []

        def inOrderTraverse(node):

            if (not node):
                return

            left = inOrderTraverse(node.left)
            self.vals.append(node.val)
            right = inOrderTraverse(node.right)

            return
        
        def buildBalancedTree(l, r):

            if (l > r):
                return
            
            mid = (l + r) // 2
            node = TreeNode(val = self.vals[mid])
            node.left = buildBalancedTree(l, mid - 1)
            node.right = buildBalancedTree(mid + 1, r)

            return node
        
        inOrderTraverse(root)
        return buildBalancedTree(0, len(self.vals) - 1)
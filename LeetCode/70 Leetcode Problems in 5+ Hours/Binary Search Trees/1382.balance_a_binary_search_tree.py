# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.node_vals = set()

        # Traverse the nodes in-order
        def inOrderTraversal(node):

            if (not node):
                return
            
            inOrderTraversal(node.left)
            self.node_vals.add(node.val)
            inOrderTraversal(node.right)

            return

        # Then have a function to build in accordance to 
        def buildBalancedBST(l, r):
            
            if (l > r):
                return None
            
            mid = ((r - l) // 2) + l 

            node = TreeNode(val = self.node_vals_lst[mid])
            node.left = buildBalancedBST(l, mid-1)
            node.right = buildBalancedBST(mid+1, r)

            return node

        inOrderTraversal(root)
        self.node_vals_lst = list(self.node_vals)
        return buildBalancedBST(0, len(self.node_vals_lst)-1)

        # Have a main
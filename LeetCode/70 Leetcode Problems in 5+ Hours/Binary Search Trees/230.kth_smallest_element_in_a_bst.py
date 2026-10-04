# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
        # Use the hard limit of 1, if we encounter 1, then return 1
        res = []

        if ((k == 1) and ((root.left == None) and (root.right == None))): return root.val

        def _traverse(root: TreeNode) -> int:
            nonlocal res

            if (not root):
                return

            if (len(res) == k):
                return res[-1]
            
            # We'll use In-order traversal

            left = _traverse(root.left)
            res.append(root.val)
            # print(res, root.val)
            if (len(res) == k):
                return res[-1]
            right = _traverse(root.right)

            return left or right

        ans = _traverse(root)

        if ans: 
            return ans 
        else:
            return 0
            
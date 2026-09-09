# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # init max_dia
        max_dia = 0

        # create a helper function to calculate the depth of the tree
        def _helper(node: Optional[TreeNode]) -> int:

            # refer to max_depth from parent func
            nonlocal max_dia

            # when helper is called on None obj, return 0
            if not node:
                return 0

            # grab the left and right depths of the current node
            ld = _helper(node.left)
            rd = _helper(node.right)
 
            # grab the diameter at the perspective of the current node
            dia = ld + rd
            max_dep = max(dia, max_dia)

            # then grab the max_dia across all traverse nodes by comparing max btwn max_dia and current diameter
            max_dia = max(max_dia, dia)

            # return max depth of the left or right + 1 (current node)
            return max(ld, rd) + 1

        # call the helper on root
        _helper(root)
        # return the max_dia
        return max_dia


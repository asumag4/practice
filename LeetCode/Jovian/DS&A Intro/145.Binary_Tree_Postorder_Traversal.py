# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        r = []
        
        def traverse(root):
            if (not root):
                return
            traverse(root.left)
            traverse(root.right)
            r.append(root.val)

        traverse(root)
        return r
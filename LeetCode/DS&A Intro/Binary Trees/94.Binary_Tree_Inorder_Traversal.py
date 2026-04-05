# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # Init output and temp. stack
        output = []
        stack = []
        
        # While root and stack are still valid objs
        while stack or root: 
            # While the root obj is still valid, we'll go left
            while root:
                stack.append(root)
                root = root.left
            
            # Then when root is no longer valid, we'll get the last-landed-on-root
            root = stack.pop()    
            # Then grab the value of that
            output.append(root.val)
            # Then go right 
            root = root.right
            
        # Return the output stack
        return output
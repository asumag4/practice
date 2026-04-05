# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        # If root is empty, return empty list 
        if (not root):
            return []

        # Create stack with root node and empty result list 
        output = []
        stack = [root]

        # 1. While stack isn't empty        
        while (stack): 
            # 1a. Pop the top node 
            node = stack.pop()
            # 1b. Add its value to result
            output.append(node.val) 
            # 1c. Push right child first (goes to bottom of stack)
            if (node.right):
                stack.append(node.right)
            # 1d. Push left child second (gets processed first due to LIFO)
            if (node.left):
                stack.append(node.left)
        
        # Return 
        return output
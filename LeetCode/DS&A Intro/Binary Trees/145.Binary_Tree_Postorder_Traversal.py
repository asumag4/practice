# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case: if theres nothing then return it 
        if (not root):
            return []

        # Init a new output and stack queue
        output = []
        stack = [root]

        # Use while loop to go over the stack
        while (stack):
            node = stack.pop()
            if (node.left):
                stack.append(node.left)
            if (node.right):
                stack.append(node.right)
            output.append(node.val)
        
        return output[::-1]
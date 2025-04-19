        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root) -> list[int]:

        # Set the out parameters 
        nodes = [] 
        out = []

        # Have a handling case 
        if root == None:
            return out

        # Set the root in a list of nodes to handle 
        nodes = [root]

        # While there are still nodes to handle; record the current node; get the right, and get then the left
        while nodes: 
            node = nodes.pop()
            out.append(node.val)
            if node.right != None:
                nodes.append(node.right)
            if node.left != None: 
                nodes.append(node.left) 

        # Return the recorded nodes 
        return out
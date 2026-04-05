# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # The philophy is:
        # -> Grab the left subtree 
        # -> Then find the right most node of the left subtree
        # -> Then append the right subtree to the right-most-node of the left subtree

        if (not root):
            return root
        if (root.val == key):
            return self.generateSubTree(root)

        dummy = root

        while (root):

            if (key < root.val):
                # Go left
                if (root.left) and (root.left.val == key):
                    root.left = self.generateSubTree(root.left)
                    break
                else:
                    root = root.left
            else:
                # Go right
                if (root.right) and (root.right.val == key):
                    root.right = self.generateSubTree(root.right)
                    break
                else:
                    root = root.right      

        return dummy    

    def generateSubTree(self, node):
        # This is in the context that `node` is the node that needs to get replaced
        if (not node.left):
            return node.right
        if (not node.right):
            return node.left

        rightSubtree = node.right
        leftNode = node.left
        # Appending node = right-most-node @ left-subtree
        appendingNode = self.findRightMostNode(node.left)
        appendingNode.right = rightSubtree
        return leftNode

    def findRightMostNode(self, node):
        if (node.right):
            return self.findRightMostNode(node.right)
        return node
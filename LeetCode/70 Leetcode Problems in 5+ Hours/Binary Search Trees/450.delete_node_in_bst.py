# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if (not root):
            return None

        if ((root.left == None) and (root.right == None) and (root.val == key)):
            return None

        # Should use post-order, because we will evaluate the the root
        # node, and we'll want to reassign 

        def reassignLeftChild(node, left):

            if (node.val > left.val):
                node.left = left
                return node
            else:
                return reassignLeftChild(node.left, left)

        def postOrderTraverse(node, prev, rel):

            if (not node):
                return 
            
            left = postOrderTraverse(node.left, node, "l")
            right = postOrderTraverse(node.right, node, "r")
            
            # Handle if node is the key
            if (node.val == key):

                if (rel == "l"):
                    prev.left = right
                    if (not right.left):
                        right.left = left
                    else:
                        right.left = reassignLeftChild(node, left)
                if (rel == "r"):

                    prev.right = right
                    if (not right.left):
                        right.left = left
                    else:
                        right.left = reassignLeftChild(node, left)

            return node

        return postOrderTraverse(root, None, None)
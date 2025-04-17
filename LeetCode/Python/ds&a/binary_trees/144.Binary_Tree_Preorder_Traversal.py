        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root) -> list[int]:

        # Initialize an empty array 

        # Have an error handling case for when root == False 

        # Save the root inside a `nodes` list (to be handled)

        # While theres still nodes to handle 

        # Handle the last node in the `nodes`

        # Get the value 

        # Qeue the right node to be handled if exists 

        # Qeue the left node to be handled if exists 

        # NOTE: the beauty is behind the order of right -> left to handle; it always ensures that the left node will be handled first because of the .pop() 

        # Return res 
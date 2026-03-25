# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        node_vals = set()
        q = deque([root])

        while q:

            # Take the node out
            node = q.popleft()

            if (not node):
                continue

            if ((k - node.val) in node_vals):
                return True

            q.append(node.left)
            q.append(node.right)

            node_vals.add(node.val)

        return False 
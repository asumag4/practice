# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:

        # Base cases
        if (not root):
            return []

        if ((not root.left) and (not root.right)):
            return [root.val]

        # BFS -> queue
        # Have a holder list of all the nodes within a level -> dump to queue
        nodes = [root]
        max_per_lvl = []
        max_at_lvl = float('-inf')
        
        while (nodes):
            
            max_at_lvl = float('-inf')
            q = deque(nodes)
            nodes = []

            while (q):
                node_i = q.popleft()

                max_at_lvl = max(max_at_lvl, node_i.val)

                if node_i.left: nodes.append(node_i.left)
                if node_i.right: nodes.append(node_i.right)

            max_per_lvl.append(max_at_lvl)

        return max_per_lvl



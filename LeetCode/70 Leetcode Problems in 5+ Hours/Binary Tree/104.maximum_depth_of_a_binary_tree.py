# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0

        q = deque([(root, 1)])
        max_depth = 1

        while q:
            node, depth = q.pop()
            # print(node.val, depth)

            if (node.left == None) and (node.right == None):
                max_depth = max(depth, max_depth)
            if (node.left):
                q.append((node.left, depth + 1))
            if (node.right):
                q.append((node.right, depth + 1))
        
        return max_depth
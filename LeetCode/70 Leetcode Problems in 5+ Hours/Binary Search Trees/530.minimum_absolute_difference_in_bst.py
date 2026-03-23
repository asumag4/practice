# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# NOTE: not the most optmial solution because I have nested for-loops, creating n^2 complexity

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        vals = deque()

        def traverseAndRecord(node):

            if (not node):
                return 
            
            nonlocal vals
            vals.append(node.val)

            traverseAndRecord(node.left)
            traverseAndRecord(node.right)

            return
        
        traverseAndRecord(root)
        # print(vals)
        min_val = max(vals)
        # print(min_val)
        for _ in range(len(vals)):
            val = vals.popleft()
            for j in range(len(vals)):
                min_val = min(min_val, abs(val - vals[j]))
            vals.append(val)
        
        return min_val
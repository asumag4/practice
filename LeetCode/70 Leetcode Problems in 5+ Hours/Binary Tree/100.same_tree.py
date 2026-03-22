# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p_deque = deque([p])
        q_deque = deque([q])

        while p_deque and q_deque:

            p_node = p_deque.popleft()
            q_node = q_deque.popleft()

            if (p_node == None) and (q_node == None):
                continue
            elif p_node == None: 
                return False
            elif q_node == None:
                return False

            if p_node.val != q_node.val:
                return False

            p_deque.append(p_node.left)
            q_deque.append(q_node.left)

            p_deque.append(p_node.right)
            q_deque.append(q_node.right)

        return True 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if (not root):
            return []
        
        def markChildrenNodes(nodes : deque):
            
            # print("=========================")
            # print(nodes)

            if (not nodes):
                return []

            q = deque()
            res = []

            while nodes:
                node = nodes.popleft()

                if (node == None):
                    continue

                res.append(node.val)

                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None

            # print("--- Children Nodes: -----------")
            # print(q)
            # print("-------------------------------")
            childrenNodes = markChildrenNodes(q)
            
            # print("Output:")
            # print(res)
            # print(childrenNodes)
            
            res1 = [res]
            if childrenNodes:
                res1.extend(childrenNodes) 

            return res1[:]
        
        return markChildrenNodes(deque([root]))


        


            
            
            

            

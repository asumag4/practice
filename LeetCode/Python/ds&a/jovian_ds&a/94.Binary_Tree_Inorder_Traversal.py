# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- Solution by CodeNinjas ---

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        
        # Go to the left most node while saving each node you go through (each node is a left node)    
        out = []
        nodes = []

        while root or nodes:
            while root: 
                nodes.append(root) # Append to the beginning
                root = root.left
        
            root = nodes.pop()
            out.append(root.val)
            root = root.right
        
        return out

# --- TEST CASES --- 

solution = Solution()

# print(solution.inorderTraversal(root=[1,None,2,3])) # [1,3,2]


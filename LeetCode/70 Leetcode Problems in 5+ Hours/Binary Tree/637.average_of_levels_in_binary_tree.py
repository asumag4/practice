# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        # Base Case

        vals = {}

        def appendChildren(node, level):
            if (node == None):
                return 
        
            if level not in vals.keys():
                vals[level] = [node.val]
            else:
                vals[level].append(node.val)

            appendChildren(node.left, level + 1)
            appendChildren(node.right, level + 1)

        appendChildren(root, 0)

        output = []
        for nums in vals.values():
            output.append((sum(nums) / len(nums)))
        
        return output
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        root_list = []

        # Traverse the entire tree & record each number
        def traverse(node : TreeNode) -> None:

            if (not node):
                return None
            
            nonlocal root_list
            root_list.append(node.val)

            traverse(node.left)
            traverse(node.right)

            return

        traverse(root)
        # Then insert your number in the end
        root_list.append(val)
        # Sort 
        root_list.sort()
        print(root_list)

        def buildTree(vals : list) -> Optional[TreeNode]:
            
            # Base Case
            if (not vals):
                return 

            vals_len = len(vals)

            # When leaf is returned
            if (vals_len == 1):
                return TreeNode(val = vals[0], left = None, right = None)
            
            # Edge-case: for when theres only 2
            if (vals_len == 2):
                left_child = TreeNode(val = vals[0], left = None, right = None)
                parent = TreeNode(val = vals[1], left = left_child, right = None)
                return parent

            # Split
            parent_node_pos = len(vals) // 2
            # Assign left and right
            left_vals = vals[:parent_node_pos]
            right_vals = vals[parent_node_pos+1:]

            # Call buildTree on left and right for remaining nodes 
            left = buildTree(left_vals)
            right = buildTree(right_vals)

            parent = TreeNode(vals[parent_node_pos], left = left, right = right)
            return parent
        
        return buildTree(root_list)

        # Then build your tree again recursively
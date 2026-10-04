/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int res = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        _traverse(root);
        return res;
    }

    private int _traverse(TreeNode root) {

        if (root == null) {
            return 0;
        }

        int left = _traverse(root.left);
        int right = _traverse(root.right);

        res = Math.max(res, left + right);

        return Math.max(left + 1, right + 1);

    }
}
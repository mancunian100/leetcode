/*
 * @lc app=leetcode id=105 lang=java
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (39.75%)
 * Total Accepted:    204.8K
 * Total Submissions: 515.2K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * Given preorder and inorder traversal of a tree, construct the binary tree.
 * 
 * Note:
 * You may assume that duplicates do not exist in the tree.
 * 
 * For example, given
 * 
 * 
 * preorder = [3,9,20,15,7]
 * inorder = [9,3,15,20,7]
 * 
 * Return the following binary tree:
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        TreeNode tree = new TreeNode(preorder[0]);
        if (preorder.length == 1) {
            return tree;
        } else {
            int root = 0;
            while (inorder[root] != preorder[0]) {
                root += 1;
            }
            int[] inleft = Arrays.copyOfRange(inorder, 0, root);
            int[] inright = Arrays.copyOfRange(inorder, root + 1, inorder.length);
            int[] preleft = Arrays.copyOfRange(preorder, 1, root + 1);
            int[] preright = Arrays.copyOfRange(preorder, root + 1, preorder.length);
            tree.left = buildTree(preleft, inleft);
            tree.right = buildTree(preright, inright);
        }
        return tree;
    }
}


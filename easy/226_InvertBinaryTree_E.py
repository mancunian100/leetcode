# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        myTree = root
        if myTree.left is None and myTree.right is None:
            return root
        myTree.left, myTree.right = myTree.right, myTree.left
        self.invertTree(myTree.left)
        self.invertTree(myTree.right)
        return root
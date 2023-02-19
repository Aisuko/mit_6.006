#!/usr/bin/env python
# 112.Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        """
        We need to calculate every path for the whole tree, and comapre them to the target
        How to calculate the value for the path?
        """
        if not root:
            return False
        # if use recursive, while should not be here.
        if not root.left and not root.right and targetSum-root.val==0:
            return True
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)

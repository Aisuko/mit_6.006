#!/usr/bin/env python
# 101.Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        """
        How to do this?
        Shall we need a data structure?
        Shall we need an iteration?
        """
        if not root:
            return False
        stack=[]
        stack.append(root.right)
        stack.append(root.left)

        while stack:
            left=stack.pop()
            right=stack.pop()
            if not left and not right:
                continue
            if not left or right or left.val!=right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

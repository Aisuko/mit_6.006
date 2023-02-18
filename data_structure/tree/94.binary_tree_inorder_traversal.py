#!/usr/bin/env python
# 94.Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self,root):
        """
        left-->root-->right
        """
        if not root:
            return root
        res,stack=[],[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                return res
            node=stack.pop()
            res.append(node.val)
            root=node.right
        return res

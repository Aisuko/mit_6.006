#!/usr/bin/env python
# 144. Binary Tree Preorder Traversal

class Solution:
    def preorderTraversal(self, root):
        """
        root-left-right
        """
        if not root:
            return root
        res,stack=[],[]
        while root or stack:
            while root:
                stack.append(root)
                res.append(root.val)
                # root-->left
                root=root.left
            if not stack:
                return res
            # left --> right
            node=stack.pop()
            root=node.right
        return res

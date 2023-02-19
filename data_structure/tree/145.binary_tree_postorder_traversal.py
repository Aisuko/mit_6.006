#!/usr/bin/env python
# 145. Binary Tree Postorder Traversal


class Solution:
    def postordertraversal(self,root):
        """
        left-->right-->root
        https://www.youtube.com/watch?v=p4GFQRyZpgg
        """
        if not root:
            return root
        
        stack=[root]
        res=[]
        while stack:
            # What is the next?
            # follow left-->right-->root
            node=stack.pop()
            if type(node)==int:
                res.append(node)
            elif node:
                stack.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

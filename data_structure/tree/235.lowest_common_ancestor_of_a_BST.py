#!/usr/bin/env python
# 235. Lowest Common Ancestor of a Binary Search Tree

def lowestCommonAncestor(root,p,q):
    """
    Return 'TreeNode'
    """
    if not root:
        return root
    if p.val>q.val:
        return lowestCommonAncestor(root,q,p)
    if root.val<p.val:
        return lowestCommonAncestor(root.left,p,q)
    if root.val>q.val:
        return lowestCommonAncestor(root.right, p,q)

    
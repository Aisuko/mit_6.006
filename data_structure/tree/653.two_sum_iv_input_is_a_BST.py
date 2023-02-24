#!/usr/bin/env python
# 653. Two Sum IV - Input is a BST

def findTarget(root,k):
    """
    Return bool
    """
    if not root:
        return False
    stack=[root]
    # We do not know which of two numbers can sum to k, so we need 
    # change our idea to check the sum
    s=set()
    for i in stack:
        if k-i.val in s:
            return True
        s.add(i.val)
        if i.left:
            stack.append(i.left)
        if i.right:
            stack.append(i.right)
    return False

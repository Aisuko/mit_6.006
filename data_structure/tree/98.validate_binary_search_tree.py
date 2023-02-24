#!/usr/bin/env python
# 98. Validate Binary search tree

def isValidBST(root): #-> bool
    """
    Return bool

    Defination for BST:
    1,left<root<right
    2,both left and right subtrees must also be BST
    """
    stack=[]
    pre=None
    while True:
        while root:
            stack.append(root)
            root=root.left
        if not stack:
            return True
        node=stack.pop()
        if pre and pre.val>=node.val:
            return False
        pre=node
        root=root.right
    
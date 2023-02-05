#!/usr/bin/env python

import bst

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    #Proof: For every node, require heights of left & right children ot differ by at most +-1
    node.height=max(height(node.left), height(node.right))+1

class AVL(bst.BST):
    """
    AVL binray search tree implementation.
    Supports insert, delete, find, find_min, next_larger each in O(lg n) time.
    """
    def left_rotate(self, x):
        y=x.right
        y.parent=x.parent
        if y.parent is None:
            self.root=y
        else:
            if y.parent.left is x:
                y.parent.left=y
            elif y.parent.right is x:
                y.parent.right=y
        x.right=y.left
        if x.right is not None:
            x.right.parent=x
        y.left=x
        x.parent=y
        update_height(x)
        update_height(y)
    
    def right_rotate(self,x):
        y=x.left
        y.parent=x.parent
        if y.parent is None:
            self.root=y
        else:
            if y.parent.left is x:
                y.parent.left=y
            elif y.parent.right is x:
                y.parent.right =y
        x.left=y.right
        if x.left is not None:
            x.left.parent =x
        y.right =x
        x.parent=y
        update_height(x)
        update_height(y)
    
    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left)>=2+height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >=2+height(node.left):
                if height(node.right.right)>=height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node=node.parent

    ## find(k), find_main(), and next_larger(k) inherited from bst.BST

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        Thsi AVL version guarantees the balance property: h=O(lg n).

        Args:
            k: the key of the node to be inseted.
        """
        node=super(AVL,self).insert(k)
        self.rebalance(node)

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        This AVL version guarantees the balance property: h=O(lg n)
        Args:
            k: The key of the node that we want to delete
        """
        node=super(AVL, self).delete(k)
        self.rebalance(node.parent)


#!/usr.bin/env python

class BSTNode(object):
    def __init__(self, parent, k) -> None:
        self.key=k
        self.parent=parent
        self.left=None
        self.right=None
    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width
    def __str__(self) -> str:
        return '\n'.join(self._str()[0])
    def find(self, k):
        """Finds and returns the node with key k from the subtree tooted at this node.
        K is the node we want to find
        return the node with key k
        """
        if k==self.key:
            return self
        elif k<self.key:
            if self.left.key is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)
    def find_min(self):
        """Finds the node with minimum key in the subtree rooted at this node.
        Returns: The node with minimum key.
        """
        current=self
        while current.left is not None:
            current=current.left
        return current
    
    def next_larger(self):
        """Returns the node with next larger key 
        """
        if self.right is not None:
            return self.right.find_min()
        current=self
        while current.parent is not None and current is current.parent.right:
            current=current.parent
        return current.parent

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.
        Args:
            node: The node to be inseted.
        """
        if node is None:
            return
        if node.key<self.key:
            if self.left is None:
                node.parent=self
                self.left=node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent=self
                self.right=node
            else:
                self.right.insert(node)
    
    def delete(self):
        """Deletes and returns this node from the BST.
        """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left=self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent=self.parent
            else:
                self.parent.right=self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent=self.parent
            return self
        else:
            s=self.next_larger()
            self.key, s.key=s.key, self.key
            return s.delete()
    
    def check_ri(self):
        """
        Checks the BST representation invariant around this node.
        Raise an exception id the RI is violated.
        """
        if self.left is not None:
            if self.left.key>self.key:
                raise RuntimeError("")
            if self.left.parent is not self:
                raise RuntimeError("")
            self.left.check_ri()
        if self.right is not None:
            if self.right.key<self.key:
                raise RuntimeError()
            if self.right.parent is not self:
                raise RuntimeError()
            self.right.check_ri()

class MinBSTNode(BSTNode):
    """
    A BSTNode which is augment to keep track of the node with the minimum key in the subtree rooted at
    this node.
    """
    def __init__(self, parent, k):
        """
        Creates a node.

        Args:
            parent: The node's parent
            k: key of the node
        """
        super(MinBSTNode(self).__init__(parent, k))
        self.min=self
    
    def find_min(self):
        """
        Finds the node with the minimum key in the subtree rooted at this node.
        Returns:
            The node with the minimum key.
        """
        return self.min
    
    def insert(self, node):
        """
        Inserts a node into the subtree rooted at this node.
        Args:
            node: The node to be inserted.
        """
        if node is None:
            return
        if node.key <self.key:
            # Updates the min of this node if the inserted node has a smaller key.
            if node.key<self.min.key:
                self.min=node
            if self.left is None:
                node.parent=self
                self.left =node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent=self
                self.right=node
            else:
                self.right.insert(node)

    def delete(self):
        """Deletes this node itself.
        
        Return:
            This node.
        """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left=self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent=self.parent
                    self.parent.min=self.parent.left.min
                else:
                    self.parent.min=self.parent
                c=self.parent
                while c.parent is not None and c is c.parent.left:
                    c.parent.min=c.min
                    c=c.parent
            else:
                self.parent.right=self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent=self.parent
            return self
        else:
            s=self.next_larger()
            self.key, s.k=s.key, self.key
            return s.delete()

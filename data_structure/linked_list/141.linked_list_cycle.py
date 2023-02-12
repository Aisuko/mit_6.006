#!/usr/bin/env python
# 141. Linked List Cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Here is a concept for check cyclic Linked list is two pointers,
        * one is normal(or move one)
        * another is normal+1(move two)
        Also were called as slow and fast pointers
        And if they meet(equal to) each other, here is a cycle.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return False
        
        slow=head
        fast=head.next

        # we should keep eyes on their value should not be none.
        # because we need to use their next or next.next point's value

            # Please be sure the value of next.next is not None and use it.
            # boarder limitation

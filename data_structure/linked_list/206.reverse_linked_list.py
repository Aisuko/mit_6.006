#!/usr/bin/env python
# 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        """
        A linked list can be reversed either iteratively or recursively.
        The time complexity for them are all O(n).
        """
        
        # iteratively
        #TODO
        cur=head
        pre=None
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre

        # recursion
        #TODO
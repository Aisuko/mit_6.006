#!/usr/bin/env python
# 83 Remove Duplicates from Sorted List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        """
        """
        curr=head
        while curr:
            while curr.next and curr.next.val==curr.val:
                if curr.val==curr.next.val:
                    curr.next=curr.next.next
            curr=curr.next
        return head

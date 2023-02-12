#!/usr/bin/env python
# 203. Remove Linked List Elements

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        """
        They want to head, so here need to have a head store prev head
        
        Time complexity:
        O(n)
        """
        pass
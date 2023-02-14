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
        # for the exmaple 2
        #return new head then set a new head
        # why do not check head? beacuse there is no necceserary to check next
        # and if the head is first element then it need more steps to deal with
        curr=head
        final=head
        while curr:
            if curr.val==val:
                # we know here we catch the element equal to val, but we need to make sure
                # it is the first node or not
                # How to know if it is the first element in the linked list?, because prev never change 
                # at the first time
                if curr==final:
                    head=head.next
                    final=final.next
                else:
                    # unlink the node from linked list
                    final=final.next
            else:
                if curr!=final:
                    final=final.next    
            curr=curr.next
        return head

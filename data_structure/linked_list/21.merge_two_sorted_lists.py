#!/usr/bin/env python
# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        l1 and l2 are sorted in non-decreasing order is useful
        Time:
        O(m+n)
        """
        # The basic situation needs to check
        # # Compare their value and recursive
        # iterative solution
        
        # if we merge two sorted in non-decreasing order linked list,
        # merge their common area then apeend the rest of their nodes
        
        # make sure you have two one as the return, another as the current
 

        #exapmple 2-3
        if not list1 or not list2:
            return list1 or list2
        
        # how to iteration and compare them with eachother
        
        # recursive: where and how to recusrive
        # Due to achieve recursion, we need to make sure it can be recusrive by the specific conditions
        # so write recursive 
        if list1.val< list2.val:
            list1=self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2=self.mergeTwoLists(list1,list2.next)
            return list2
        
        # ITERATION
        # things are totally different from recusrive, we need to pay attention on node.next in every loop
        
        # if we use iteration, so we need define final and current ListNode
        final=curr=ListNode(0)

        while list1 and list2:
            if list1.val<list2.val:
                # because curr is ListNode(0), and we can append next node
                curr.next=list1.val
                list1=list1.next
            else:
                curr.next=list2.val
                list2=list2.next
            curr=curr.next
        # be careful the rest of list1 and list2
        curr.next=list1 or list2
        # be careful the first node is [0], so return final.next
        return final.next


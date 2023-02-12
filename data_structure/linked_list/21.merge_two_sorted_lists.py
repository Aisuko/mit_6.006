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
        # if not list1 or not list2:
        #     return list1 or list2
        # # Compare their value and recursive
        # if list1.val<list2.val:
        #     list1.next=self.mergeTwoLists(list1.next,list2)
        #     return list1
        # else:
        #     list2.next=self.mergeTwoLists(list1,list2.next)
        #     return list2

        # iterative solution
        tempHead=cur=ListNode(0)
        while list1 and list2:
            if list1.val<list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        
        cur.next =list1 or list2
        return tempHead.next

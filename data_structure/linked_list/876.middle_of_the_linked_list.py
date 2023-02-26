#!/usr/bin/env python
# 876. Middle of the Linked List

class Solution:
    def middleNode(self, head):
        """
        Return ListNode
        use the slow and fast pointers to count on the element
        slow=slow.next
        fast=head.next.next
        so, if fast traversal to the end of the linked list, slow is must at the second middle element of the list
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

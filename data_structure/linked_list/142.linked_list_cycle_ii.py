#!/usr/bin/env python
# 142.Linked List Cycle II

class Solution:
    def detectCycle(self, head):
        """
        the length of fast pointer travel is equal to the slow pointer travel to the cycles' entry
        This is also related to the slow and fast pointers traversal path
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                newSlow=head
                while (newSlow!=fast):
                    newSlow=newSlow.next
                    fast=fast.next
                return newSlow
        return None

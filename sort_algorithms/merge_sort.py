#!/usr/bin/env python
#
# Best     O(nlogn)
# Average  O(nlogn)
# Worst    O(nlogn)
# Momery   1
# Stable   Yes
# Method   Insertion


###########################
# Insertion is more effective for small part of data, 
# so we shold split data at first.
# 
# At the second step we need to check two side's elements one by one.


def merge(left,right):
    """
    Use comparising
    """
    



def merge_sort(m):
    """
    Split the data into two part first
    """
    # check if the length for m is <=1 and then split the list into two part
    if not m:
        return m
    # if we want to merge, we need to split it to two array
    middle=len(m)//2
    left=m[:middle]
    right=m[middle:]


    return merge(left,right)


la=[3,5,4,6,12,8,2,1]

print(merge_sort(la))
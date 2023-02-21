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
    result=[]
    l,r=0,0
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r-=1
    if left:
        result.extend(left[l:])
    if right:
        result.extend(right[r:])
    return result



def merge_sort(m):
    """
    Split the data into two part first
    """
    # check if the length for m is <=1 and then split the list into two part
    if len(m)<=1:
        return m
    # how to split it into two parts, module 
    middle=len(m)//2
    left=m[:middle]
    right=m[middle:]

    # Do not forget sort left and right
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)


la=[3,5,4,6,12,8,2,1]

print(merge_sort(la))
#!/usr/bin/env python
# 217. Contains Duplicate

def containsDuplicate(nums) -> bool:
    """Given an integer array nums, return true if any value appears at least twice in the arary

    Time: O(n)
    If there is another request that it needs to count the number has appearances, there may need more process.
    """
    # l={}
    # for i in nums:
    #     if i in l:
    #         return True
    #     else:
    #         # Random to use a integer number
    #         l[i]=0
    # return False

    return not len(nums)==len(set(nums))

# Case1
print(containsDuplicate([1,2,3,1]))
# Case2
print(containsDuplicate([1,2,3,4]))
# Case3
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
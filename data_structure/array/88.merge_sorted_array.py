#!/usr/bin/env python
# 88. Merge Sorted Array
# Array, Two pointers Sorting

def merge(nums1,m,nums2,n):
    """
    None do not return anything, modify nums1 in-place instead
    Need O(n+m)
    """

    # if m==0:
    #     nums1=nums2[:n] 
    #     return nums1 # There cannnot pass the LeetCode checking
    # if n==0:
    #     return nums1[:m]
    
    i=m-1
    j=n-1
    final=(m+n-1)

    while final >=0:
        if i>=0 and j>=0:
            if (nums2[j]>nums1[i]):
                nums1[final]=nums2[j]
                final-=1
                j-=1
            else:
                nums1[final]=nums1[i]
                final-=1
                i-=1
        # if is not necessary, because the while loop will check the condition
        elif j>=0:
            nums1[final]=nums2[j]
            final-=1
            j-=1
        else:
            break
    return nums1    


print(merge([1,2,3,0,0,0],3,[2,5,6],3))

print(merge([1],1,[],0))

print(merge([0],0,[1],1))
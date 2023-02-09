#!/usr/bin/env python
# Searching in a Hash map is O(1)
# Counter objects in collections in Python is provided to support convenient and rapid tallies.

import collections
class Solution:
    def intersect(self, nums1, nums2):
        """collections.Counter has take a most important role

        Time complexity: I assume it is O(n), n=len(nums2)
        """
        if len(nums1)>len(nums2):
            self.intersect(nums2,nums1)
        cNums1=collections.Counter(nums1)
        finalList=[]
        for i in nums2:
            if cNums1[i]>0:
                finalList.append(i)
                cNums1[i]-=1
        return finalList

if __name__=="__main__":
    print(Solution().intersect([1,2,2,1],[2,2]))
    print(Solution().intersect([4,9,5],[9,4,9,8,4]))

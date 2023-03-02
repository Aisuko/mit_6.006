#!/usr/bin/env python
# 704. Binary Search

class Solution:
    def search(self, nums,target):
        """
        """

        # iterative
        start=0
        end=len(nums)-1
        # middle=(start+end)//2
        # while start<=end:
        #     if target==nums[middle]:
        #         return middle
        #     elif target>nums[middle]:
        #         start=middle+1
        #     else:
        #         end=middle-1
        # return -1
        return self.bs(nums,start,end,target)

        # recursive
    def bs(self, nums,start,end,target):
        if start>end:
            return -1
        middle=(start+end)//2
        if target<nums[middle]:
            end=middle-1
        elif target>nums[middle]:
            start=middle+1
        else:
            return middle
        return self.bs(nums,start,end, target)

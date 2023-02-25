#!/usr/bin/env python
# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        if not nums:
            return nums
        res=[]
        cur=0
        for i in nums:
            cur+=i
            res.append(cur)
        return res

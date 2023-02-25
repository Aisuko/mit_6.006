#!/usr/bin/env python
# 724. Find Pivot Index

class Soluction:
    def pivotIndex(self, nums):
        """
        Return int
        left ++
        right--
        left++=right--
        """
        left=0
        right=sum(nums)
        for k,v in enumerate(nums):
            left+=v
            if left==right:
                return k
            right-=v
        return -1

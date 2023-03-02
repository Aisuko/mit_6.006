#!/usr/bin/env python
# 278. First Bad Version

# The isBadVersion API is already defined for you.
def isBadVersion(version: int):
    return True

class Solution:
    def firstBadVersion(self,n):
        """
        Return int
        This question is a little bit make people feel confused
        """
        start=0
        end=n
        res=0
        while start<=end:
            middle=(start+end)//2
            if isBadVersion(middle):
                res=middle
                end=middle-1
            else:
                start=middle+1
        return res



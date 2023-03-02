#!/usr/bin/env python
# 392. Is Subdequence

class Solution:
    def isSubdequence(self,s,t):
        """
        Return bool
        s is the primary string than t
        so,
        * len(s)<=len(t)
        * s not is True
        * t not is False
        """
        # if s is "", return True
        # if not s:
        #     return True
        # elif not t:
        #     return False
        # # isSubdequence(abc,ahbgdc)
        # #  isSubsequence(bc,hbgdc)
        # #   isSubsequence(bc,bgdc)
        # #    isSubsequence(c,gdc)
        # #     isSubsequence(c,dc)
        # #      isSubsequence(c,c)
        # #       isSubsequence("","")
        # return self.isSubdequence(s[1:],t[1:]) if s[0]==t[0] else self.isSubdequence(s,t[1:])

        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
            if i==len(s):
                return True
        return False

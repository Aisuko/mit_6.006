#!/usr/bin/env python
# 409 Longest Palindrome

class Solution:
    def longestPalindrome(self,s):
        """
        Return int
        """

        l=set()
        for c in s:
            if c not in l:
                l.add(c)
            else:
                l.remove(c)
        return len(s)-len(l)+1 if len(l)>0 else len(s)

print(Solution().longestPalindrome("abccccdd"))

#!/usr/bin/env python
# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s):
        """
        Find the first non-repeating character in it and return its index.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        dic={}
        dicAllTime={}
        for k,v in enumerate(s):
            if v not in dicAllTime:
                dic[v]=k
                dicAllTime[v]=k
            # How about if v in s? Remove it
            elif v in dic:
                dic.pop(v)
        # Here only no repeat character
        if len(dic)>0:
            # Here need the first non-repeating character
            fnc=list(dic.keys())[0]
            return dic[fnc]
        else:
            return -1


if __name__=="__main__":
    print(Solution().firstUniqChar("leetcode"))
    print(Solution().firstUniqChar("loveleetcode"))
    print(Solution().firstUniqChar("aabb"))

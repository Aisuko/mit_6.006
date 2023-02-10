#!/usr/bin/env python
# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s):
        """
        Find the first non-repeating character in it and return its index.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        tempFirst={}
        allElement={}

        for k,v in enumerate(s):
            if v not in allElement:
                tempFirst[v]=k
                allElement[v]=k
            # check if element is in unique hashmap
            elif v in tempFirst:
                tempFirst.pop(v)

        # if there is unique element then return its position
        if (len(tempFirst)>0):
            res=list(tempFirst.keys())[0]
            return tempFirst[res] # otherwise return -1
        else:
            return -1


if __name__=="__main__":
    print(Solution().firstUniqChar("leetcode"))
    print(Solution().firstUniqChar("loveleetcode"))
    print(Solution().firstUniqChar("aabb"))

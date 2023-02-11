#!/usr/bin/env python
#242.Valid Anagram
import collections
class Solution:
    def isAnagram(self, s, t):
        """
        O(len(s)+len(t)+len(dic.items()))
        """
        dic=collections.defaultdict(int)
        for i in s:
            dic[i]+=1
        for i in t:
            dic[i]-=1
        #TODO


if __name__=="__main__":
    print(Solution().isAnagram("anagram","nagaram"))
    print(Solution().isAnagram("rat","car"))
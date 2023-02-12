#!/usr/bin/env python
#242.Valid Anagram
import collections
class Solution:
    def isAnagram(self, s, t)-> bool:
        """
        O(len(s)+len(t)+len(dic.items()))
        """
        dic=collections.defaultdict(int)
        for i in s:
            dic[i]+=1
        for i in t:
            dic[i]-=1
        # here needs items to return key-values pairs 
        # for dic
        for k,v in dic.items():
            if v!=0:
                return False
        return True


if __name__=="__main__":
    print(Solution().isAnagram("anagram","nagaram"))
    print(Solution().isAnagram("rat","car"))
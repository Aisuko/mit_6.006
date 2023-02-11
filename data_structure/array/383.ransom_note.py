#!/usr/bin/env python
#383.Ransom Note

class Solution:
    def canConstruct(self,ransomNote,magazine):
        """
        How to check str1 includes str2?

        Time complexity: O(m+n)
        """
        # even we use hash table, there is not necessary key
        dic={}
        for i in ransomNote:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in magazine:
            if i in dic:
                # According to the request, 
                # * "aa" ->"aab" is true.
                # * "aa" -> "ab" is false
                
                #TODO


if __name__ == "__main__":
    print(Solution().canConstruct("a","b"))
    print(Solution().canConstruct("aa","ab"))
    print(Solution().canConstruct("aa","aab"))
        
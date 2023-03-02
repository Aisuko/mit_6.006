#!/usr/bin/env python
# 205.Isomorphic Strings

def isIsomorphic(s,t):
    """
    Return bool
    """
    l=[s.index(i) for i in s]
    r=[t.index(i) for i in t]
    return l==t

s="egg"
t="add"

print(isIsomorphic(s,t))

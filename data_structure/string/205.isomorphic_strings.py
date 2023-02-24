#!/usr/bin/env python
# 205.Isomorphic Strings

def isIsomorphic(s,t):
    """
    Return bool
    """
    ls=[s.index(i) for i in s]
    lt=[t.index(j) for j in t]
    return ls==lt

s="egg"
t="add"

print(isIsomorphic(s,t))

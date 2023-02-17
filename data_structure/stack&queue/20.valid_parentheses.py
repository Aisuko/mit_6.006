#!/usr/bin/env python
# 20.Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        """
        What we should pay attention on it?
        * the structure for string is '(){}[]' which is as the couple,so we can use stack(LIFO) to save the data.
        * we can simulate stack by using list[] in Python
        """
        stack=[]
        for i in s:
            if i in ('(','{','['):
                stack.append(i)
            # if i is the right-side parentheses, 
            # and we need to make sure it's left-side is the last element that we append to stack
            elif i==')' and len(stack)!=0 and stack[-1]=='(':
                # because it is the parentheses, we cannot compare it them directly,
                # so we can count the length of stack
                stack.pop()
            elif i==']' and len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            elif i=='}' and len(stack)!=0 and stack[-1]=='{':
                stack.pop()
            else:
                return False
        return len(stack)==0
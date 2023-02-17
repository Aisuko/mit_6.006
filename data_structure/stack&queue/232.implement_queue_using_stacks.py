#!/usr/bin/env python
# 232.Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        # we use python, so we use list to simulate queue
        self._data=[]
        

    def push(self, x: int) -> None:
        """
        Keep in mind the push operation, add new element to the queue
        """
        self._data.append(x)
        

    def pop(self) -> int:
        """
        Because of queue, FIFO, return the first element
        """
        return self._data.pop(0)
        

    def peek(self) -> int:
        """
        return peek, but does not change the items in the queue
        """
        return self._data[0]
        

    def empty(self) -> bool:
        """
        if len(self.data)>0 empty is false
        else empty is False
        """
        return not self._data
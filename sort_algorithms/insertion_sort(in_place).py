#!/usr/bin/env python
# Best n
# Average n^2
# Worst n^2

def insertion_sort(array):
    """
    We implement insertion sort by compare current and previous element
    and try to exchange their position
    """
    if not array:
        return array
    for i in range(1, len(array)):
        # loop all the elements in the array
        # let's compare the elements
        prevIndex=i-1
        current=array[i]
        #TODO


#!/usr/bin/env python
#53.maximum Subarray
#dynamic programming problem: 

def maxSubArray(nums) -> int:
    """
    Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

    As the problem mentioned that "divide and conquer approach". 
    This is a concept in dynamic programming problem which it is a strategy for programming.
    What is the DP and why need that?
    See here: https://hololandscape.github.io/aisuko/docs/mit_6_006_07/

    Time: O(n) because we only have one time iteration
    """
    lenNums=len(nums)
    if lenNums==0:
        return 0
    temSum=maxSum=nums[0]
    for i in range(1,lenNums):
        # How to comapre the sums, in DP, the most important step is memoized
        temSum=max(temSum+nums[i],nums[i])
        maxSum=max(temSum,maxSum)
    return maxSum

# Case 1
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# Case 2
print(maxSubArray([1]))
# Case 3
print(maxSubArray([5,4,-1,7,8]))

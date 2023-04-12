#!/usr/bin/env python
# 118.Pascal's Triangle

class Solution:
    def generate(self, numRows):
        """
        Know about how to calculate value on every subArray is important
        n=len(numRows)
        O(len(n*(n-1)))
        """
        #Preparing
        finalArray=[]
        finalArray.append([1])

        # Basic e.g: #2
        if numRows==1:
            return finalArray
        
        # how to calculate elements in every new row
        for i in range(numRows-1):
            tempArray=[1]
            # if here has an iteration from i, especially j+1, the iteration above needs to be range(numRows-1)
            # And there won not execute at the first time
            for j in range(i):
                # Here is difficult to know how to calculate the value, but it is easy to know how to get the value if 
                # you know the index of the value. You actually have a 2d list, and you need to know how to get the value.
                tempArray.append(finalArray[i][j]+finalArray[i][j+1])
            tempArray.append(1)
            finalArray.append(tempArray)
        return finalArray

if __name__ =="__main__":
    print(Solution().generate(5))

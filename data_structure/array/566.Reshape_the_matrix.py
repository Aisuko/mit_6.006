#!/usr/bin/env python
# 566.Reshape the matrix

class Solution:
    def matrixReshape(self, mat, r, c):
        """
        Please be sure you know how to keep tracking the length of the elements and 
        it should be no more than columns. 
        Time complexity: O(m*n)
        """
        count=0
        finalArray=[]
        tempArray=[]
        if r*c!=len(mat)*len(mat[0]):
            return mat
        for l in mat:
            for i in l:
                tempArray.append(i)
                count+=1
                if count==c:
                    finalArray.append(tempArray)
                    tempArray=[]
                    count=0
        return finalArray

if __name__ =="__main__":
    print(Solution().matrixReshape([[1,2],[3,4]],1,4))

#!/usr/bin/env python
# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        """
        O(log(m * n)) is the necessary for time complexity.
        O(log n)
        """
        row=len(matrix)
        column=len(matrix[0])
        # The basic factor of divide and conquer is have a start and end point
        start=0
        end=row*column-1
        # Traversing
        # Key point: How to find what index in the matrix has the 5th element while traversing: row-wise and column-wise
        while start<=end:
            mid=(start+end)//2 # integer rather than float
            # get sub-row and sub-column
            # Here we use column to divide mid which is the number of rows traversed
            r=mid//column
            # The remainder of this operation is the column elements are need to check
            c=mid%column
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                start=mid+1
            else:
                end=mid-1
        return False

if __name__ =="__main__":
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))

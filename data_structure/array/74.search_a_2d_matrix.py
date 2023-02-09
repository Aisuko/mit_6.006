#!/usr/bin/env python
# 74.Search a 2D matrix

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        """
        O(log(m * n)) is the necessary for time complexity.
        """


        row=len(matrix)
        column=len(matrix[0])-1

        start, final=0, row*column-1
        while start<=final:
            mid=(start+final)//2
            r=mid//column
            c=mid%column
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]< target:
                start=mid+1
            else:
                final=mid-1
        return False


        # for i in range(row):
        #     if target <matrix[i][column]:
        #         if target in matrix[i]:
        #             return True
        # return False

if __name__ == "__main__":
    Solution().searchMatrix([[1]],1)
    Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
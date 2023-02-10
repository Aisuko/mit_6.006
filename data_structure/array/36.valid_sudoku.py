#!/usr/bin/env python
# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board):
        """
        There are two strategies here:
        9x9
          * First, check if there any same element in a row
          * Second, check if there any same element in a column
        3x3
          * check if there any same elment in sub-row or sub-column
        """
        row=len(board)
        column=len(board[0])
        

        # The checking for row
        for i in board:
            # Every row cannot has the same elements
            elements=[]
            for j in i:
                if j in elements:
                    return False
                elif j !=".":
                    elements.append(j)


        # The checking for column
        for i in range(row):
            elements=[]
            for j in range(9):
                if board[j][i] in elements:
                    return False
                elif board[j][i]!=".":
                    elements.append(board[j][i])
        
        # The checking for 3x3 box
        # How to check them?
        for i in range(0,9,3):
            for j in range(0,9,3):
                elements=[]
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] in elements:
                            return False
                        elif board[r][c] !="." and board[r][c] not in elements:
                            elements.append(board[r][c])
        
        return True

if __name__ =="__main__":
    validSudoku=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    inValidSudoku=[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(validSudoku))
    print(Solution().isValidSudoku(inValidSudoku))
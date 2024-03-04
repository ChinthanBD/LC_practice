# https://leetcode.com/problems/sudoku-solver/description/
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if self.isValid(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True 

    def isValid(self, board, row, col, num):
        # Check if the current number 'num' is already present in the same row or column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        # Check if the current number 'num' is already present in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        # If 'num' is not found in the same row, column, or subgrid, it's valid
        return True


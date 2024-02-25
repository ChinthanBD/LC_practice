from typing import List
# class Solution:
#     def mark_zero(self, matrix, i, j, m,n):
    #     for row in range(m):
    #         if matrix[row][j] != 0:
    #             matrix[row][j] = 'q'
    #     for col in range(n):
    #         if matrix[i][col] != 0:
    #             matrix[i][col] = 'q'


    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     m = len (matrix)
    #     n = max(len(row) for row in matrix)

    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 self.mark_zero(matrix, i, j, m, n)

    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 'q':
    #                 matrix[i][j] = 0
    # First pass to mark the zeros and the first element of rows and columns
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        # Variables to track if the first row and first column need to be zeroed out
        row_zero = False
        col_zero = False

        # Check if the first row contains any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break

        # Check if the first column contains any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break

        # Iterate through the matrix and use the first row and first column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Iterate through the matrix again and zero out cells based on markings
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if necessary
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if necessary
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0

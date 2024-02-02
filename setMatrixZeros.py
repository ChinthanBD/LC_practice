from typing import List
class Solution:
    def mark_zero(self, matrix, i, j, m,n):
        for row in range(m):
            if matrix[row][j] != 0:
                matrix[row][j] = 'q'
        for col in range(n):
            if matrix[i][col] != 0:
                matrix[i][col] = 'q'
        return matrix


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len (matrix)
        n = max(len(row) for row in matrix)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[:][:] = self.mark_zero(matrix, i, j, m, n)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'q':
                    matrix[i][j] = 0

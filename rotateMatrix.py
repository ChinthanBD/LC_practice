# https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        res = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ele = matrix[i][j]

                dest_i,dest_j = j, m - 1 - i
                res[dest_i][dest_j] = ele
        
        for i in range(m):
            for j in range(n):  
                matrix[i][j] = res[i][j]
                
### Above is using extra array, Not so good :( 

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()
                            